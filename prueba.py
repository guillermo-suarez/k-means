from funciones import abrirCSV, ch_score
from kmeans import marcarCentroidesAleatorios, kMeans

cant_pruebas = 10
puntos = abrirCSV('Datasets/dataset_1.csv')
#se prueba en todo el rango de los k posibles
for k in range(2,6):
    ch_score_promedio = 0
    for i in range(cant_pruebas):
        bgss_prueba_i = 0
        wgss_prueba_i = 0
        ch_score_prueba_i = 0
        centroides, puntos = marcarCentroidesAleatorios(k, puntos)
        iteraciones = kMeans(k, puntos, centroides)
        ch_score_prueba_i = ch_score(puntos, iteraciones)
        ch_score_promedio +=  ch_score_prueba_i
    ch_score_promedio /= cant_pruebas 
    print("Para k = " + str(k) + " se obtuvo un CH promedio de " + str(ch_score_promedio))