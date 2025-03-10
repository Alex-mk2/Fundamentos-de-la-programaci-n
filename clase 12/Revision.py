import requests #peticiones
import smtplib ### Usar para la opcion de correo opcion 10
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt #el de los graficos
from email.mime.text import MIMEText

url = "https://www.sismologia.cl"
repuesta = requests.get(url)
contenido = repuesta.text #el .text es de BS es para obtener el texto sin las etiquetas
soup = BeautifulSoup(contenido, 'lxml')
##print(soup.prettify()) para revisar las etiquetas del html procesado por el parsel o nalizador sintactico## 
tabla = soup.find("table" ,class_='sismologia')
titulos = tabla.find_all("th")

columnas= []
for e in titulos:
    titulo = e.text
    columnas.append(titulo)

datos = []
filas = tabla.find_all("tr")
for fila in filas[1:]:  #Ojo empieza del 1 porque la primera ya esta que es el encabezado de las columnas o la primera fila
    celdas = fila.find_all("td")
    datosFila = [celda.text.strip() for celda in celdas]
    datos.append(datosFila)
#ya de aqui empezamos con el pandas###
df = pd.DataFrame(datos,columns= columnas)

df[['Fecha', 'Direccion']] = df['Fecha Local / Lugar (2)'].str.split('\n', expand=True)
df = df.drop(columns=['Fecha Local / Lugar (2)'])
#df = df[['Fecha', 'Direccion', 'ProfundidadProf.', 'MagnitudMag.']]
df[['Direccion', 'Ciudad']] = df['Direccion'].str.split(' de ', n=1, expand=True)
df = df[['Fecha', 'Ciudad', 'Direccion', 'ProfundidadProf.', 'MagnitudMag.']]
df['ProfundidadProf.'] = df['ProfundidadProf.'].str.replace('km', '').astype(int)
df['MagnitudMag.'] = pd.to_numeric(df['MagnitudMag.'], errors='coerce')
df['Fecha']= pd.to_datetime(df['Fecha'], format='%Y-%m-%d %H:%M:%S', errors='coerce')
df.columns = df.columns.str.replace('ProfundidadProf.', 'Profundidad en km')
df.to_csv("TablaSismologia.csv", index=False, encoding='latin-1') # Caracteres en La letra "ü" se representa de manera diferente en UTF-8 y Latin-1 (ISO-8859-1):

print(df)
print(df.dtypes)

#### Funciones del programa ####

def rankingMayorMagnitud(df):
    return df.nlargest(3, 'MagnitudMag.')

def profundidadDia(df):
    hoy = datetime.now().date()
    datosDia = df[df['Fecha'].dt.date == hoy]
    return datosDia['Profundidad en km'].sum()

def sismoMenorMag(df):
    return df.nsmallest(1, 'MagnitudMag.')

def sismosIntervaloTiempo(df, dia, horaInicio, horaFin):
    añoActual = datetime.now().year
    mesActual = datetime.now().month
    fecha = pd.to_datetime(f'{añoActual}-{mesActual:02d}-{dia:02d}', format='%Y-%m-%d').date()
    inicio = pd.to_datetime(horaInicio, format='%H:%M:%S').time()
    fin = pd.to_datetime(horaFin, format='%H:%M:%S').time()

    datos_dia = df[df['Fecha'].dt.date == fecha]
    datos_intervalo = datos_dia[(datos_dia['Fecha'].dt.time >= inicio) & (datos_dia['Fecha'].dt.time <= fin)]
    return datos_intervalo

def ultimoSismo(df):
    ultimo = df.iloc[-1]
    return ultimo

def tiempoUltimosismo(df):
    ultimoSismo = df.iloc[0]  # Selecciona la primera fila del DataFrame
    tiempoPrimerSismo = ultimoSismo['Fecha']
    ahora = datetime.now()
    tiempoTranscurrido = ahora - tiempoPrimerSismo
    return tiempoTranscurrido, ultimoSismo

def graficoSismosPorCiudad(df):
    ciudadcontador = df['Ciudad'].value_counts()
    plt.figure(figsize=(10, 6))
    plt.bar(ciudadcontador.index, ciudadcontador.values)
    plt.xticks(rotation=45)
    plt.title('Numero de sismos por ciudad')
    plt.xlabel('Ciudad')
    plt.ylabel('Número de sismos')
    plt.show()

def graficoSismosPorMagnitud(df):
    promedioMagnitudes = df.groupby('Ciudad')['MagnitudMag.'].mean()
    plt.figure(figsize=(12, 8))
    plt.bar(promedioMagnitudes.index, promedioMagnitudes.values, color='purple')
    plt.xlabel('Ciudad')
    plt.ylabel('Magnitud Promedio')
    plt.title('Promedio de Magnitudes de Sismos por Ciudad')
    plt.xticks(rotation=90)
    plt.show()

def graficoDistribucionSismosPorHora(df):
    df['Hora'] = df['Fecha'].dt.hour
    conteoXHora = df['Hora'].value_counts().sort_index()
    plt.figure(figsize=(12, 8))
    plt.bar(conteoXHora.index, conteoXHora.values, color='lightgreen')
    
    plt.xlabel('Hora del Dia')
    plt.ylabel('Numero de Sismos')
    plt.title('Distribución de Sismos por Hora del Dia')
    plt.xticks(range(24))
#    plt.grid()
    plt.show()
def enviarCorreo(ultimoSismo):
    remitente = 'dansealiste@gmail.com'
    destinatario = input('correo del destinatario: ')
    asunto = 'Último sismo registrado'

    cuerpo = f"Datos del último sismo:\n\n{ultimoSismo.to_string()}"

    mensaje = MIMEText(cuerpo, _charset='latin-1')
    mensaje['Subject'] = asunto
    mensaje['From'] = remitente
    mensaje['To'] = destinatario

    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()
    
    servidor.login(remitente, '12aliste34')
    servidor.sendmail(remitente, destinatario, mensaje.as_string())
    servidor.quit()

    print("Correo enviado correctamente.")

#### menu del programa ####
print("Bienvenido al programa de analisis de sismos, Proyecto de programacion de la universidad finis terrae")
print("Ingrese el numero correspondiente a la opcion que desea seleccionar:")
print("1: Ranking de los 3 sismos de mayor magnitud")
print("2: Profundidad total de sismos del dia actual")
print("3: Sismo de menor magnitud")
print("4: Sismos en un intervalo de tiempo")
print("5: Informacin del ultimo sismo")
print("6: Tiempo transcurrido desde el ultimo sismo")
print("7: grafico de sismos por ciudad registrada")
print("8: grafico de Sismos Por promedio de Magnitud")
print("9: grafico de Distribucion de Sismos Por Hora")
print("10: Enviar por correo datos del ultimo sismo registrado")
print("0: Salir del programa")

menu = True
while menu == True:
    opcion = input('Ingrese la opción de la función que quiere utilizar o ingrese 0 para finalizar: ')

    if opcion == '1':
        print('Ranking con los 3 sismos de mayor magnitud:')
        print(rankingMayorMagnitud(df))
    elif opcion == '2':
        resultado = profundidadDia(df)
        print(f'Profundidad acumulada del día actual: {resultado} km')
    elif opcion == '3':
        print('Sismo de menor magnitud:')
        print(sismoMenorMag(df))

    elif opcion == '4':
            dia = int(input('Ingrese el día del mes (1-31): '))
            horaInicio = input('Ingrese la hora de inicio (HH:MM:SS): ')
            horaFin = input('Ingrese la hora de fin (HH:MM:SS): ')
            sismos = sismosIntervaloTiempo(df, dia, horaInicio, horaFin)
            if sismos.empty:
                print("No se encontraron sismos en el intervalo especificado.")
            else:
                print(f'Sismos ocurridos el día {dia} del mes actual entre {horaInicio} y {horaFin}:')
                print(sismos)

    elif opcion == '5':
        print('Ultimo sismo:')
        print(ultimoSismo(df))

    elif opcion == '6':
        tiempoTranscurrido, datosUltimo = tiempoUltimosismo(df)
        print(f'Tiempo transcurrido desde el último sismo: {tiempoTranscurrido}')

    elif opcion == '7':
        graficoSismosPorCiudad(df)

    elif opcion == '8':
        graficoSismosPorMagnitud(df)
    elif opcion == '9':
        graficoDistribucionSismosPorHora(df)
    elif opcion == '10':
        ultimo_sismo = ultimoSismo(df)
        enviarCorreo(ultimo_sismo)
    elif opcion == '0':
        menu = False
        break
    else:
        print('Opcion invalida') 