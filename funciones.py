import csv
import math as m

def abrirCSV(path: str):
    with open(path, 'r') as dataset:
        reader = csv.reader(dataset, delimiter=";")
        encabezados = next(reader)
        datos = list(reader)
    puntos = []
    for dato in datos:
        x = float(dato[0].replace(',', '.'))
        y = float(dato[1].replace(',', '.'))
        cluster = int(0)
        punto = [x, y, cluster]
        puntos.append(punto)
    return puntos

def separarPorClusters(k, puntos):
    clusters = []
    for i in range(k):
        cluster = []
        clusters.append(cluster)
    for punto in puntos:
        clusters[punto[2] - 1].append([punto[0], punto[1]]) 
    return clusters

def calcularDistancia(puntoA, puntoB):
    return m.sqrt((puntoA[0]-puntoB[0])**2 + (puntoA[1]-puntoB[1])**2)

def actualizarCentroide(cluster, centroide):
    if len(cluster) > 0:
        valoresX = [punto[0] for punto in cluster]
        valoresY = [punto[1] for punto in cluster]
        x = min(valoresX) + ((max(valoresX) - min(valoresX)) / 2.0)
        y = min(valoresY) + ((max(valoresY) - min(valoresY)) / 2.0)
    else:
        x = centroide[0]
        y = centroide[1]
    nuevoCentroide = [x, y]
    return nuevoCentroide

#-------------A partir de acá son funciones específicas para Calinski-Harabasz-------------

def norma_sin_raiz(puntoA, puntoB):
    #Función que simula el calculo de la norma entre dos puntos. No utiliza la raíz cuadrada
    #debido a que en CH se eleva al cuadrado la norma, haciendo así que se simplique la raíz.
    return ((puntoA[0]-puntoB[0])**2 + (puntoA[1]-puntoB[1])**2)

def calculo_bgss(dataset, centroides, clusters):
    #Función que devuelve la dispersión inter-cluster.
    #El baricentro es el centroide del dataset.
    sumatoria = 0
    cant_puntos = 0
    distancia_baricentro = 0
    baricentro = actualizarCentroide(dataset, 0)
    for i, cluster in enumerate(clusters):
        cant_puntos = len(cluster)
        distancia_baricentro = norma_sin_raiz(centroides[i], baricentro)
        sumatoria += (cant_puntos * distancia_baricentro)
    return sumatoria

def calculo_wgss(centroides, clusters):
    #Función que devuelve la dispersión intra-cluster.
    sumatoria_total = 0
    for i, cluster in enumerate(clusters):
        sumatoria = 0
        for punto in cluster:
            sumatoria += norma_sin_raiz(centroides[i], punto)
        sumatoria_total += sumatoria
    return sumatoria_total

def ch_score(puntos, iteraciones):
    #Función que permite calcular el indice Calinski-Harabasz.
    #Se utiliza solamente la iteración final, por eso el [-1].
    #UI: siglas para última iteración.
    cant_puntos = len(puntos)
    bgss = 0
    wgss = 0
    score = 0
    centroides_UI = iteraciones[-1][0]
    clusters_UI = iteraciones[-1][1]
    k = len(centroides_UI)
    bgss = calculo_bgss(puntos, centroides_UI, clusters_UI)
    wgss = calculo_wgss(centroides_UI, clusters_UI)
    score = ((bgss/wgss) * ((cant_puntos - k)/(k-1)))
    return score

#-------------Hasta acá son funciones específicas para Calinski-Harabasz-------------