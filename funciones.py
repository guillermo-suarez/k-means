import csv
import math as m

def abrirCSV(path: str):
    with open(path, 'r') as dataset:
        reader = csv.reader(dataset, delimiter=";")
        encabezados = next(reader)
        datos = list(reader)
    puntos = []
    etiquetas = []
    for dato in datos:
        x = float(dato[0].replace(',', '.'))
        y = float(dato[1].replace(',', '.'))
        punto = [x, y]
        puntos.append(punto)

        etiqueta = int(0)
        etiquetas.append(etiqueta)
    return puntos, etiquetas

def separarPorClusters(k, puntos, etiquetas):
    clusters = []
    for i in range(k):
        cluster = []
        clusters.append(cluster)
    for i, punto in enumerate(puntos):
        clusters[etiquetas[i] - 1].append(punto) 
    return clusters

def calcularDistancia(puntoA, puntoB):
    return m.sqrt((puntoA[0]-puntoB[0])**2 + (puntoA[1]-puntoB[1])**2)

def calcularDistanciaCuadrada(puntoA, puntoB):
    return ((puntoA[0]-puntoB[0])**2 + (puntoA[1]-puntoB[1])**2)

def getPuntoMedio(grupoDePuntos):
    nuevoCentroide = None
    if len(grupoDePuntos) > 0:
        valoresX = [punto[0] for punto in grupoDePuntos]
        valoresY = [punto[1] for punto in grupoDePuntos]
        x = sum(valoresX) / len(valoresX)
        y = sum(valoresY) / len(valoresY)
        nuevoCentroide = [x, y]
    return nuevoCentroide

def calcularBGSS(dataset, centroides, clusters):
    # Función que devuelve la dispersión inter-cluster.
    # El baricentro es el centroide del dataset.
    BGSS = 0
    baricentro = getPuntoMedio(dataset)
    for i, cluster in enumerate(clusters):
        nCluster = len(cluster)
        distanciaBaricentro = calcularDistanciaCuadrada(centroides[i], baricentro)
        BGSS += (nCluster * distanciaBaricentro)
    return BGSS

def calcularWGSS(centroides, clusters):
    # Función que devuelve la dispersión intra-cluster.
    WGSS = 0
    for i, cluster in enumerate(clusters):
        sumatoria = 0
        for punto in cluster:
            sumatoria += calcularDistanciaCuadrada(centroides[i], punto)
        WGSS += sumatoria
    return WGSS

def getCHScore(centroides, puntos, etiquetas):
    # Función que permite calcular el indice Calinski-Harabasz.
    N = len(puntos)
    k = len(centroides)
    clusters = separarPorClusters(k, puntos, etiquetas)
    BGSS = calcularBGSS(puntos, centroides, clusters)
    WGSS = calcularWGSS(centroides, clusters)
    chScore = ((BGSS / WGSS) * ((N - k) / (k - 1)))
    return chScore