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
        dist = float(10000.0)
        punto = [x, y, cluster, dist]
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

def actualizarCentroides(k, puntos):
    centroides = []

    clusters = separarPorClusters(k, puntos)

    for cluster in clusters:
        if len(cluster) > 0:
            primerPunto = cluster[0]
            
            minX = primerPunto[0]
            maxX = primerPunto[0]

            minY = primerPunto[1]
            maxY = primerPunto[1]

            for punto in cluster:
                if punto[0] < minX:
                    minX = punto[0]
                if punto[0] > maxX:
                    maxX = punto[0]

                if punto[1] < minY:
                    minY = punto[1]
                if punto[1] > maxY:
                    maxY = punto[1]
            
            x = minX + ((maxX - minX) / 2.0)
            y = minY + ((maxY - minY) / 2.0)

            centroides.append([x, y])

    return centroides