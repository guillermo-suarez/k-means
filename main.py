from funciones import abrirCSV, separarPorClusters
from kmeans import marcarCentroidesAleatorios, kMeans

import matplotlib.pyplot as plt

k = 5
puntos = abrirCSV('Datasets/dataset_1.csv')
centroides, puntos = marcarCentroidesAleatorios(k, puntos)
iteraciones = kMeans(k, puntos, centroides)

# Se buscan los máximos y mínimos por eje
minX = 9999.0
maxX = -9999.0
minY = 9999.0
maxY = -9999.0
for punto in puntos:
    # Encontrar valor máximo y mínimo de eje X
    if punto[0] < minX:
        minX = punto[0]
    elif punto[0] > maxX:
        maxX = punto[0]
    
    # Encontrar valor máximo y mínimo de eje Y
    if punto[1] < minY:
        minY = punto[1]
    elif punto[1] > maxY:
        maxY = punto[1]

# Definir límites de los ejes para los gráficos
# Se le suma 10% (0.1) a ambos lados a cada eje
if(minX < 0):
    limMinX = minX + (minX * 0.1)
else:
    limMinX = minX - (minX * 0.1)
if(maxX < 0):
    limMaxX = maxX - (maxX * 0.1)
else:
    limMaxX = maxX + (maxX * 0.1)

if(minY < 0):
    limMinY = minY + (minY * 0.1)
else:
    limMinY = minY - (minY * 0.1)
if(maxY < 0):
    limMaxY = maxY - (maxY * 0.1)
else:
    limMaxY = maxY + (maxY * 0.1)    

# Como son 5 clústers como máximo, 5 colores
colores = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 0],
    [0, 1, 1]
]

plt.figure()

x = [punto[0] for punto in puntos]
y = [punto[1] for punto in puntos]
plt.scatter(x, y, label = 'Punto sin asignar' , color = [1, 1, 1], s = 20.0, edgecolors = 'black')

for h, centroide in enumerate(centroides):
        x = centroide[0]
        y = centroide[1]
        plt.scatter(x, y, label = 'Centroide ' + str(h + 1), color = colores[h], s = 100.0, edgecolors = 'black')

plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.xlim(limMinX, limMaxX)
plt.ylim(limMinY, limMaxY)
plt.title('Estado inicial')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.show(block = False)

for i, iteracion in enumerate(iteraciones):
    plt.figure()

    centroides = iteracion[0]
    puntos = iteracion[1]
    clusters = separarPorClusters(k, puntos)

    for j, cluster in enumerate(clusters):
        x = [punto[0] for punto in cluster]
        y = [punto[1] for punto in cluster]
        plt.scatter(x, y, label = 'Punto del clúster ' + str(j + 1), color = colores[j], s = 20.0, edgecolors = 'black')

    for h, centroide in enumerate(centroides):
        x = centroide[0]
        y = centroide[1]
        plt.scatter(x, y, label = 'Centroide ' + str(h + 1), color = colores[h], s = 100.0, edgecolors = 'black')

    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.xlim(limMinX, limMaxX)
    plt.ylim(limMinY, limMaxY)
    plt.title('Iteración ' + str(i + 1))
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

    plt.tight_layout()
    plt.show(block = False)

plt.show()