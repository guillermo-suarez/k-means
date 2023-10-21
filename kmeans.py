import copy
import random as rnd

from funciones import calcularDistancia, getPuntoMedio, separarPorClusters, getCHScore

def getSemillasAleatorios(k, puntos):
    centroides = []
    n = len(puntos)
    for i in range(k):
        j = rnd.randint(0, n - 1)
        while puntos[j] in centroides:
            j = rnd.randint(0, n - 1)
        centroides.append([puntos[j][0], puntos[j][1]])
    return centroides

def getSemillasHeuristica(k, puntos):
    centroides = []
    n = len(puntos)
    # PRIMER CENTROIDE: el punto mas lejano al centroide del dataset
    baricentro = getPuntoMedio(puntos)
    distancias_baricentro = []
    for j, punto in enumerate(puntos):
        distancia_al_baricentro = calcularDistancia(baricentro, punto)
        distancias_baricentro.append(distancia_al_baricentro)
    pto = distancias_baricentro.index(max(distancias_baricentro))
    centroides.append([puntos[pto][0], puntos[pto][1]])
    # RESTO DE LOS CENTROIDES: el punto que maximice su distancia a su centroide mas cercano (de lo que se hayan definido hasta el momento)
    for i in range(1, k):        
        # Calculamos los siguientes centroides a partir de las distancias mínimas:
        distancias_minimas = []
        for j, punto in enumerate(puntos):
            distancia_minima = float('inf')
            for centroide in centroides:
                distancia = calcularDistancia(centroide, punto)
                distancia_minima = min(distancia_minima, distancia)
            distancias_minimas.append(distancia_minima)
        # Seleccionamos el punto con mayor distancia al centroide    
        pto = distancias_minimas.index(max(distancias_minimas)) 
        centroides.append([puntos[pto][0], puntos[pto][1]])
    return centroides

def kMeans(k, puntos, etiquetas, centroides):
    iteraciones = []
    umbral = round((len(puntos) * 0.01) + 0.5)
    puntosQueCambiaron = umbral + 1
    while puntosQueCambiaron >= umbral:
        puntosQueCambiaron = 0
        # Para cada punto...
        for i, punto in enumerate(puntos):
            # ...calculamos las distancias con todos los otros centroides
            distancias = [calcularDistancia(centroide, punto) for centroide in centroides]
            # Buscamos, entre todas esas distancias, la más chica e identificamos a que clúster ahora pertenecería el punto
            for j, distancia in enumerate(distancias):
                if distancia == min(distancias):
                    nroClusterMin = j + 1
            # Si va a cambiar el Nº de cluster al que pertenece el punto, se aumenta en 1 el contador de puntos que cambiaron de cluster
            if nroClusterMin != etiquetas[i]:
                puntosQueCambiaron = puntosQueCambiaron + 1
            # Se reemplaza en que cluster está
            etiquetas[i] = nroClusterMin
        # Después de terminar la iteración...
        # Se crea una copia de todos los centroides
        centroidesIteracion = copy.deepcopy(centroides)
        # Se crea una copia de como quedaron las etiquetas
        etiquetasIteracion = copy.deepcopy(etiquetas)
        chScoreIteracion = getCHScore(centroidesIteracion, puntos, etiquetasIteracion)
        # Ahora sí, creamos la iteración y la agregamos a la lista de iteraciones
        iteracion = [centroidesIteracion, etiquetasIteracion, puntosQueCambiaron, chScoreIteracion]
        iteraciones.append(iteracion)
        # Si al menos 1 punto cambió de cluster, se actualizan los centroides
        if puntosQueCambiaron > 0:
            nuevosCentroides = []
            for i, cluster in enumerate(separarPorClusters(k, puntos, etiquetas)):
                if getPuntoMedio(cluster) == None:
                    nuevoCentroide = centroides[i]
                else:
                    nuevoCentroide = getPuntoMedio(cluster)
                nuevosCentroides.append(nuevoCentroide)
            centroides = nuevosCentroides
    return copy.deepcopy(iteraciones)