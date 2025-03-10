import numpy as np

# Respuestas correctas (pauta)
respuestas_correctas = np.array(['d', 'c', 'c', 'd', 'b', 'a', 'c', 'a', 'd', 'c', 'b', 'c'])

# Respuestas de los participantes
respuestas_participantes = np.array([
    ['d', 'c', 'c', 'd', 'c', 'd', 'a', 'c', 'd', 'd', 'd', 'd'],
    ['c', 'c', 'c', 'd', 'a', 'b', 'b', 'c', 'c', 'd', 'b', 'b'],
    ['d', 'c', 'c', 'd', 'c', 'c', 'c', 'a', 'd', 'a', 'b', 'c'],
    ['d', 'd', 'c', 'd', 'b', 'c', 'c', 'd', 'd', 'b', 'b', 'a'],
    ['a', 'c', 'b', 'd', 'b', 'c', 'c', 'a', 'd', 'b', 'd', 'd'],
    ['d', 'a', 'c', 'd', 'b', 'c', 'c', 'b', 'd', 'a', 'b', 'c'],
    ['d', 'c', 'b', 'd', 'b', 'b', 'b', 'a', 'b', 'c', 'b', 'c'],
    ['b', 'a', 'c', 'd', 'b', 'c', 'a', 'c', 'c', 'c', 'a', 'c'],
    ['d', 'c', 'd', 'a', 'a', 'a', 'a', 'd', 'c', 'a', 'a', 'c'],
    ['d', 'c', 'b', 'd', 'd', 'b', 'a', 'a', 'a', 'b', 'b', 'c'],
    ['b', 'c', 'd', 'd', 'c', 'a', 'd', 'c', 'b', 'a', 'c', 'd'], 
    ['d', 'a', 'c', 'a', 'd', 'c', 'a', 'a', 'c', 'b', 'a', 'd'],
    ['d', 'a', 'c', 'b', 'c', 'd', 'd', 'b', 'b', 'c', 'a', 'd'],
    ['a', 'c', 'c', 'd', 'b', 'a', 'c', 'd', 'c', 'c', 'b', 'c'],
    ['d', 'c', 'b', 'd', 'c', 'a', 'b', 'c', 'c', 'a', 'a', 'c'],
    ['d', 'd', 'c', 'b', 'c', 'c', 'd', 'd', 'c', 'd', 'a', 'b'],
    ['a', 'c', 'd', 'd', 'a', 'd', 'c', 'c', 'a', 'c', 'd', 'c'],
    ['d', 'c', 'b', 'b', 'c', 'd', 'd', 'c', 'a', 'a', 'c', 'd'],
    ['d', 'c', 'c', 'b', 'a', 'a', 'c', 'c', 'b', 'c', 'a', 'a'],
    ['b', 'c', 'c', 'd', 'd', 'c', 'c', 'c', 'b', 'a', 'a', 'c'],
    ['d', 'c', 'c', 'd', 'c', 'b', 'd', 'd', 'c', 'a', 'b', 'c'],
    ['d', 'c', 'c', 'd', 'c', 'c', 'd', 'd', 'b', 'c', 'd', 'b'],
    ['d', 'a', 'c', 'd', 'a', 'b', 'c', 'd', 'a', 'b', 'b', 'd'],
])

# Identificar los errores (respuestas incorrectas)
errores = (respuestas_participantes != respuestas_correctas) & (respuestas_participantes != '')

# Contar el número de errores por pregunta
errores_por_pregunta = np.sum(errores, axis=0)

# Encontrar las preguntas con más errores
preguntas_mas_errores = np.where(errores_por_pregunta == np.max(errores_por_pregunta))[0]

errores_por_pregunta, preguntas_mas_errores + 1  # +1 para ajustar a numeración humana