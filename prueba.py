from funciones import abrirCSV, getCHScore
from kmeans import getSemillasAleatorios, getSemillasHeuristica, kMeans
import time

pruebas = 100
# Se prueba en todo el rango de los k posibles
for k in range(2, 6):
    chScorePromedio = 0
    tiempoPromedio = 0
    for i in range(pruebas):
        puntos, etiquetas = abrirCSV('Datasets/dataset_1.csv')
        inicioAlgoritmo = time.time()
        centroides = getSemillasAleatorios(k, puntos)
        iteraciones = kMeans(k, puntos, etiquetas, centroides)
        finAlgoritmo = time.time()
        centroides = iteraciones[-1][0]
        etiquetas = iteraciones[-1][1]
        chScore = getCHScore(centroides, puntos, etiquetas)
        chScorePromedio +=  chScore
        tiempoPromedio += (finAlgoritmo - inicioAlgoritmo)
    chScorePromedio /= pruebas
    tiempoPromedio /= pruebas
    print("Para k = " + str(k) + " se obtuvo un CH promedio de " + str(chScorePromedio))
    print("Cada algoritmo demoro en promedio ", str(tiempoPromedio))