import csv

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

def calcularBGSS(dataset, centroides, clusters):
    # Función que devuelve la dispersión inter-cluster.
    # El baricentro es el centroide del dataset.
    bgss = 0
    baricentro = getPuntoMedio(dataset)
    for i, cluster in enumerate(clusters):
        nCluster = len(cluster)
        distanciaBaricentro = calcularDistancia(centroides[i], baricentro)
        bgss += (nCluster * distanciaBaricentro)
    return bgss

def calcularWGSS(centroides, clusters):
    # Función que devuelve la dispersión intra-cluster.
    wgss = 0
    for i, cluster in enumerate(clusters):
        sumatoria = 0
        for punto in cluster:
            sumatoria += calcularDistancia(centroides[i], punto)
        wgss += sumatoria
    return wgss

def getCHScore(centroides, puntos, etiquetas):
    # Función que permite calcular el indice Calinski-Harabasz.
    n = len(puntos)
    k = len(centroides)
    clusters = separarPorClusters(k, puntos, etiquetas)
    bgss = calcularBGSS(puntos, centroides, clusters)
    wgss = calcularWGSS(centroides, clusters)
    chScore = ((bgss / wgss) * ((n - k) / (k - 1)))
    return chScore