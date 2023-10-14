from funciones import abrirCSV, ch_score
from kmeans import marcarCentroidesAleatorios, kMeans

pruebas = 10
# Se prueba en todo el rango de los k posibles
for k in range(2, 6):
    chScorePromedio = 0
    for i in range(pruebas):
        puntos, etiquetas = abrirCSV('Datasets/dataset_3.csv')
        centroides, puntos, etiquetas = marcarCentroidesHeuristica(k, puntos, etiquetas)
        iteraciones = kMeans(k, puntos, etiquetas, centroides)
        centroides = iteraciones[-1][0]
        etiquetas = iteraciones[-1][1]
        chScore = getCHScore(centroides, puntos, etiquetas)
        chScorePromedio +=  chScore
    chScorePromedio /= pruebas
    print("Para k = " + str(k) + " se obtuvo un CH promedio de " + str(chScorePromedio))