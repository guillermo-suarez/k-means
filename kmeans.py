import copy
import random as rnd

from funciones import calcularDistancia, actualizarCentroide, separarPorClusters

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
            # ...calculamos las distancias con todos los otros centroides
            distancias = [calcularDistancia(centroide, punto) for centroide in centroides]
            # Buscamos, entre todas esas distancias, la más chica e identificamos a que clúster ahora pertenecería el punto
            for j, distancia in enumerate(distancias):
                if distancia == min(distancias):
                    nroClusterMin = j + 1
            # Si va a cambiar el Nº de cluster al que pertenece el punto, se aumenta en 1 el contador de puntos que cambiaron de cluster
            if nroClusterMin != punto[2]:
                puntosQueCambiaron = puntosQueCambiaron + 1
            # Se reemplaza en que cluster está
            punto[2] = nroClusterMin
        # Después de terminar la iteración...
        # Se crea una copia de todos los centroides
        centroidesIteracion = copy.deepcopy(centroides)
        # Además, se crea una copia de todos los puntos con sus Nº de clúster actualizados
        puntosIteracion = copy.deepcopy(puntos)
        # Y se los divide en clústers
        clustersIteracion = separarPorClusters(k, puntosIteracion)
        # Ahora sí, creamos la iteración y la agregamos a la lista de iteraciones
        iteracion = [centroidesIteracion, clustersIteracion, puntosQueCambiaron]
        iteraciones.append(iteracion)
        # Si al menos 1 punto cambió de cluster, se actualizan los centroides
        if puntosQueCambiaron > 0:
            centroides = [actualizarCentroide(cluster, centroides[i]) for i, cluster in enumerate(separarPorClusters(k, puntos))]
    return copy.deepcopy(iteraciones)