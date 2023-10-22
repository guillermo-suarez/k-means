from funciones import abrirCSV, getCHScore
from kmeans import getSemillasAleatorios, getSemillasHeuristica, kMeans
import time

pruebas = 100
datasets = ['Datasets/dataset_1.csv', 'Datasets/dataset_2.csv', 'Datasets/dataset_3.csv']
# Se hacen estas pruebas por dataset
for dataset in datasets:
    print('\n' + dataset)
    # Se prueba en todo el rango de los k posibles
    for k in range(2, 6):
        print('\t>> Con k = ' + str(k))
        # Se corren 100 tiradas con semillas aleatorias y se considera sus valores promedios
        chScorePromedio = 0
        tiempoPromedio = 0
        for i in range(pruebas):
            puntos, etiquetas = abrirCSV(dataset)
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
        print('\t\t+ Inicialización Aleatoria (' + str(pruebas) + ' tiradas)')
        print('\t\t\t- CH Score promedio = ' + ("%.2f" % chScorePromedio))
        print('\t\t\t- Tiempo promedio de ejecución = ' + ("%.2f" % (tiempoPromedio * 1000)) + ' milisegundos')
        puntos, etiquetas = abrirCSV(dataset)
        inicioAlgoritmo = time.time()
        centroides = getSemillasHeuristica(k, puntos)
        iteraciones = kMeans(k, puntos, etiquetas, centroides)
        finAlgoritmo = time.time()
        centroides = iteraciones[-1][0]
        etiquetas = iteraciones[-1][1]
        chScore = getCHScore(centroides, puntos, etiquetas)
        tiempo = finAlgoritmo - inicioAlgoritmo
        print('\t\t+ Inicialización Heurística (k-means++)')
        print('\t\t\t- CH Score = ' + ("%.2f" % chScore) + '. Este valor es varía en un ' + ("%.2f%% con respecto al resultado por inicialización aleatoria." % (((chScore - chScorePromedio) / chScore) * 100)))
        print('\t\t\t- Tiempo de ejecución = ' + ("%.2f" % (tiempo * 1000)) + ' milisegundos' + '. Este valor es varía en un ' + ("%.2f%% con respecto al resultado por inicialización aleatoria." % (((tiempo - tiempoPromedio) / tiempo) * 100)))