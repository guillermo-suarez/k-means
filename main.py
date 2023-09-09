import csv
import random
import math as m
import matplotlib.pyplot as plt

# Cantidad de clusters
k = 5

with open("Datasets/dataset_1.csv", 'r') as dataset:
    reader = csv.reader(dataset, delimiter=";")
    encabezados = next(reader)
    puntosCSV = list(reader)

puntos = []
puntosX = []
puntosY = []

for punto in puntosCSV:
    x, y = punto[0], punto[1]
    x = float(x.replace(',', '.'))
    y = float(y.replace(',', '.'))
    puntos.append([x, y, 0])
    puntosX.append(x)
    puntosY.append(y)

# Cada punto tiene [cordX, cordY, cluster al que pertence]
# Cluster = 0 ----> todavía no se asignó un cluster

# print('Este dataset tiene ' + str(len(puntos)) + ' puntos.')

minX = puntos[0][0]
maxX = puntos[0][0]
minY = puntos[0][1]
maxY = puntos[0][1]

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

# print('El eje X va desde ' + str(minX) + ' hasta ' + str(maxX))
# print('El eje Y va desde ' + str(minY) + ' hasta ' + str(maxY))

# Crear los k centroides aleatoriamente
centroides = []
centroidesX = []
centroidesY = []
centroidesCords = []
for i in range(k):
    rndX = random.random()
    rndY = random.random()
    centX = minX + (maxX - minX) * rndX
    centY = minY + (maxY - minY) * rndY
    centroides.append([centX, centY])
    centroidesX.append(centX)
    centroidesY.append(centY)

# for i in range(0, len(centroides)):
#     print('Centroide ' + str(i + 1) + ': ' + str(centroides[i]))

# Iteración 1 - asignación de clústers
for punto in puntos:
    distancias = []
    for centroide in centroides:
        distancias.append(m.sqrt((punto[0] - centroide[0])**2 + (punto[1] - centroide[1])**2))
    distanciaMin = distancias[0]
    for i in range(0, len(distancias)):
        if distancias[i] <= distanciaMin:
            punto[2] = i + 1
            distanciaMin = distancias[i]

# Creamos la lista de clusters
clustersCords = []
for i in range(k):
    clusterX = []
    clusterY = []
    for punto in puntos:
        if(punto[2] == i + 1):
            clusterX.append(punto[0])
            clusterY.append(punto[1])
    clustersCords.append([clusterX, clusterY])

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

colores = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 0],
    [0, 1, 1]
]

# En un gráfico mostramos los puntos y los centroides resultados de la Iteración 1
plt.subplot(1, 2, 1)
plt.gca().set_facecolor((0, 0, 0, 0.75))
plt.scatter(puntosX, puntosY, label='Punto sin agrupar', color=(1, 1, 1), s=20.0, edgecolors='black')
for i in range (len(centroides)):
    plt.scatter(centroides[i][0], centroides[i][1], label='Centroide ' + str(i + 1), color=colores[i], s=100.0, edgecolors='black')
plt.xlim(limMinX, limMaxX)
plt.ylim(limMinY, limMaxY)
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Antes de agrupar')
plt.legend()

# En otro gráfico mostramos como quedarían los clusters después de la Iteración 1
plt.subplot(1, 2, 2)
plt.gca().set_facecolor((0, 0, 0, 0.75))
for i in range(len(clustersCords)):
    # print('Clúster ' + str(i + 1) + ' tiene ' + str(len(clustersCords[i][0])) + ' valores de eje X y ' + str(len(clustersCords[i][1])) + ' valores de eje Y.')
    plt.scatter(clustersCords[i][0], clustersCords[i][1], label='Punto del clúster ' + str(i + 1), color=(colores[i]), s=20.0, edgecolors='black')
for i in range (len(centroides)):
    plt.scatter(centroides[i][0], centroides[i][1], label='Centroide ' + str(i + 1), color=colores[i], s=100.0, edgecolors='black')
plt.xlim(limMinX, limMaxX)
plt.ylim(limMinY, limMaxY)
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Después de agrupar')
plt.legend()

plt.suptitle('Iteración 1 - NO SE VUELVEN A AJUSTAR LOS CENTROIDES')
plt.tight_layout()
plt.show()