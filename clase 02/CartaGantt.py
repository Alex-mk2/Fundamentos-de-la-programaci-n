import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import date2num, DateFormatter
from datetime import datetime, timedelta


# Create a DataFrame with the weeks and tasks
tasks_extended = {
    "Etapa 1: Investigación literatura y Análisis Inicial": [1],
    "Etapa 2: Construcción de Matrices de ruido": [2, 3],
    "Etapa 3: Codificación del Algoritmo NSGA-II": [4, 5],
    "Etapa 4: Ejecución del Algoritmo con toda la información biológica y Comparación con matriz de distancia biológica con ruido": [6, 7],
    "Etapa 5: Comparar los resultados obtenidos por NSGA-II con la información total vs NSGA-II con matriz de distancia biológica con ruido": [8],
    "Etapa 6: Construir el reporte técnico con los resultados obtenidos de ambos algoritmos": list(range(9, 18))
}

# Initialize an empty DataFrame
weeks = list(range(1, 18))
data = {f'Semana {i}': [] for i in weeks}
data['Tarea'] = []

# Fill the DataFrame with tasks and weeks
for task, week_list in tasks_extended.items():
    row = ['####' if i in week_list else '' for i in weeks]
    row.append(task)
    for i, week in enumerate(weeks):
        data[f'Semana {week}'].append(row[i])
    data['Tarea'].append(task)

# Create the DataFrame
df = pd.DataFrame(data, columns=['Tarea'] + [f'Semana {i}' for i in weeks])
df.set_index('Tarea', inplace=True)

# Save the DataFrame as an Excel file
df.to_excel('/mnt/data/gantt_chart_weeks.xlsx')

df
