from funciones import abrirCSV, separarPorClusters
from kmeans import marcarCentroidesAleatorios, marcarCentroidesHeuristica, kMeans
import matplotlib.pyplot as plt

def estadoInicial(csv):
    puntos, etiquetas = abrirCSV(csv)
    minX = min([punto[0] for punto in puntos])
    maxX = max([punto[0] for punto in puntos])
    minY = min([punto[1] for punto in puntos])
    maxY = max([punto[1] for punto in puntos])
    fig, ax = plt.subplots()
    limMinX = minX - ((maxX - minX) * 0.1)
    limMaxX = maxX + ((maxX - minX) * 0.1)
    limMinY = minY - ((maxY - minY) * 0.1)
    limMaxY = maxY + ((maxY - minY) * 0.1)
    x = [punto[0] for punto in puntos]
    y = [punto[1] for punto in puntos]
    ax.scatter(x, y, label = 'Punto sin asignar' , color = [1, 1, 1], s = 20.0, edgecolors = 'black')   
    ax.set_xlabel('Eje X')
    ax.set_ylabel('Eje Y')
    ax.set_xlim(limMinX, limMaxX)
    ax.set_ylim(limMinY, limMaxY)
    ax.set_title('Dataset')
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
    fig.tight_layout()
    return fig

def figsKmeans(csv, k, tipo):
    puntos, etiquetas = abrirCSV(csv)
    figInicial, iteraciones = figInicialKmeans(puntos, etiquetas, k, tipo)
    i = len(iteraciones) - 1
    figFinal = figIteracionKmeans(puntos, iteraciones, k, i)
    return figInicial, figFinal, iteraciones, k, puntos


def figInicialKmeans(puntos, etiquetas, k, tipo):    
    colores = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 1],
    [0, 1, 1]
    ]
    fig, ax = plt.subplots()
    minX = min([punto[0] for punto in puntos])
    maxX = max([punto[0] for punto in puntos])
    minY = min([punto[1] for punto in puntos])
    maxY = max([punto[1] for punto in puntos])
    limMinX = minX - ((maxX - minX) * 0.1)
    limMaxX = maxX + ((maxX - minX) * 0.1)
    limMinY = minY - ((maxY - minY) * 0.1)
    limMaxY = maxY + ((maxY - minY) * 0.1)
    if(tipo == 'h'):
        centroides, puntos, etiquetas = marcarCentroidesHeuristica(k, puntos, etiquetas)
    elif(tipo == 'a'):
        centroides, puntos, etiquetas = marcarCentroidesAleatorios(k, puntos, etiquetas)
    x = [punto[0] for punto in puntos]
    y = [punto[1] for punto in puntos]
    ax.scatter(x, y, label = 'Punto sin asignar' , color = [1, 1, 1], s = 20.0, edgecolors = 'black')   
    for h, centroide in enumerate(centroides):
        x = centroide[0]
        y = centroide[1]
        ax.scatter(x, y, label = 'Centroide ' + str(h + 1), color = colores[h], s = 100.0, edgecolors = 'black')
    ax.set_xlabel('Eje X')
    ax.set_ylabel('Eje Y')
    ax.set_xlim(limMinX, limMaxX)
    ax.set_ylim(limMinY, limMaxY)
    ax.set_title('Estado inicial')
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
    fig.tight_layout()    
    iteraciones = kMeans(k, puntos, etiquetas, centroides)
    for h, centroide in enumerate(centroides):
        x = centroide[0]
        y = centroide[1]
        ax.scatter(x, y, label = 'Centroide ' + str(h + 1), color = colores[h], s = 100.0, edgecolors = 'black')    
    return fig, iteraciones

def figIteracionKmeans(puntos, iteraciones, k, i):
    colores = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 1],
    [0, 1, 1]
    ]
    fig, ax = plt.subplots()
    minX = min([punto[0] for punto in puntos])
    maxX = max([punto[0] for punto in puntos])
    minY = min([punto[1] for punto in puntos])
    maxY = max([punto[1] for punto in puntos])
    limMinX = minX - ((maxX - minX) * 0.1)
    limMaxX = maxX + ((maxX - minX) * 0.1)
    limMinY = minY - ((maxY - minY) * 0.1)
    limMaxY = maxY + ((maxY - minY) * 0.1)
    centroides = iteraciones[i][0]
    etiquetas = iteraciones[i][1]
    cambiaron = iteraciones[i][2]
    chScore = iteraciones[i][3]
    clusters = separarPorClusters(k, puntos, etiquetas)
    for j, cluster in enumerate(clusters):
        x = [punto[0] for punto in cluster]
        y = [punto[1] for punto in cluster]
        plt.scatter(x, y, label = 'Punto del clúster ' + str(j + 1), color = colores[j], s = 20.0, edgecolors = 'black')
    for h, centroide in enumerate(centroides):
        x = centroide[0]
        y = centroide[1]
        plt.scatter(x, y, label = 'Centroide ' + str(h + 1), color = colores[h], s = 100.0, edgecolors = 'black')
    ax.set_xlabel('Eje X')
    ax.set_ylabel('Eje Y')
    ax.set_xlim(limMinX, limMaxX)
    ax.set_ylim(limMinY, limMaxY)
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
    ax.set_title('Iteración ' + str(i) + '.\nEn esta iteración ' + str(cambiaron) + ' puntos cambiaron de clúster.\nCalinski-Harabasz score: ' + ("%.2f" % chScore))
    fig.tight_layout()
    return fig