import copy
import random as rnd

from funciones import calcularDistancia, actualizarCentroides, separarPorClusters

def marcarCentroidesAleatorios(k, puntos):
    centroides = []
    n = len(puntos)
    for i in range(k):
        j = rnd.randint(0, n - 1)
        centroides.append([puntos[j][0], puntos[j][1]])
        puntos[j][2] = i + 1
    return centroides, puntos

def kMeans(k, puntos, centroides):

    iteraciones = []

    puntosQueCambiaron = 1

    while puntosQueCambiaron > 0:

        puntosQueCambiaron = 0

        # Para cada punto...
        for punto in puntos:
            nroClusterActual = punto[2]
            distanciaActual = 10000.0

            # ...calculamos las distancias con todos los otros centroides
            distancias = []
            for centroide in centroides:
                distancia = calcularDistancia(centroide, punto)
                distancias.append(distancia)

            # Buscamos, entre todas esas distancias, la más chica que, además, sea menor a la actual
            for j, distancia in enumerate(distancias):
                if distancia < distanciaActual:
                    distanciaActual = distancia
                    nroClusterActual = j + 1
            
            # Si va a cambiar el Nº de cluster, se aumenta en 1 el contador de puntos que cambiaron de cluster
            if nroClusterActual != punto[2]:
                puntosQueCambiaron = puntosQueCambiaron + 1

            # Se reemplazan los valores
            punto[2] = nroClusterActual
            punto[3] = distanciaActual
        
        iteracion = []
        iteracion.append(copy.deepcopy(centroides))
        iteracion.append(copy.deepcopy(puntos))
        iteraciones.append(iteracion)
        if puntosQueCambiaron > 0:
            centroides = actualizarCentroides(k, puntos)

    return list(iteraciones)