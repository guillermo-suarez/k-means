from funciones import abrirCSV, getCHScore
from kmeans import getSemillasAleatorios, getSemillasHeuristica, kMeans

pruebas = 10
# Se prueba en todo el rango de los k posibles
for k in range(2, 6):
    chScorePromedio = 0
    for i in range(pruebas):
        puntos, etiquetas = abrirCSV('Datasets/dataset_3.csv')
        centroides = getSemillasHeuristica(k, puntos)
        iteraciones = kMeans(k, puntos, etiquetas, centroides)
        centroides = iteraciones[-1][0]
        etiquetas = iteraciones[-1][1]
        chScore = getCHScore(centroides, puntos, etiquetas)
        chScorePromedio +=  chScore
    chScorePromedio /= pruebas
    print("Para k = " + str(k) + " se obtuvo un CH promedio de " + str(chScorePromedio))