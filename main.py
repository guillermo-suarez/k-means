from vistas import call_vistas

call_vistas()

# from funciones import abrirCSV, separarPorClusters
# from kmeans import marcarCentroidesAleatorios, marcarCentroidesHeuristica, kMeans
# import matplotlib.pyplot as plt

# k = 5
# puntos, etiquetas = abrirCSV('Datasets/dataset_3.csv')
# # centroides, puntos, etiquetas = marcarCentroidesAleatorios(k, puntos, etiquetas)
# centroides, puntos, etiquetas = marcarCentroidesHeuristica(k, puntos, etiquetas)
# iteraciones = kMeans(k, puntos, etiquetas, centroides)

# # Se buscan los máximos y mínimos por eje
# minX = min([punto[0] for punto in puntos])
# maxX = max([punto[0] for punto in puntos])
# minY = min([punto[1] for punto in puntos])
# maxY = max([punto[1] for punto in puntos])

# # Definir límites de los ejes para los gráficos
# # Se le suma 10% (0.1) a ambos lados a cada eje
# limMinX = minX - ((maxX - minX) * 0.1)
# limMaxX = maxX + ((maxX - minX) * 0.1)
# limMinY = minY - ((maxY - minY) * 0.1)
# limMaxY = maxY + ((maxY - minY) * 0.1)

# # Como son 5 clústers como máximo, 5 colores 
# colores = [
#     [1, 0, 0],
#     [0, 1, 0],
#     [0, 0, 1],
#     [1, 0, 1],
#     [0, 1, 1]
# ]

# # Mostrar el estado inicial: todos los puntos y los centroides inicializados 
# plt.figure()
# x = [punto[0] for punto in puntos]
# y = [punto[1] for punto in puntos]
# plt.scatter(x, y, label = 'Punto sin asignar' , color = [1, 1, 1], s = 20.0, edgecolors = 'black')
# for h, centroide in enumerate(centroides):
#         x = centroide[0]
#         y = centroide[1]
#         plt.scatter(x, y, label = 'Centroide ' + str(h + 1), color = colores[h], s = 100.0, edgecolors = 'black')
# plt.xlabel('Eje X')
# plt.ylabel('Eje Y')
# plt.xlim(limMinX, limMaxX)
# plt.ylim(limMinY, limMaxY)
# plt.title('Estado inicial')
# plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
# plt.tight_layout()
# plt.show(block = False)

# # Mostrar todas las iteraciones, 1 por gráfico. Sus centroides y a que clúster pertenece cada punto
# for i, iteracion in enumerate(iteraciones):
#     plt.figure()
#     centroides = iteracion[0]
#     etiquetas = iteracion[1]
#     cambiaron = iteracion[2]
#     chScore = iteracion[3]
#     clusters = separarPorClusters(k, puntos, etiquetas)
#     for j, cluster in enumerate(clusters):
#         x = [punto[0] for punto in cluster]
#         y = [punto[1] for punto in cluster]
#         plt.scatter(x, y, label = 'Punto del clúster ' + str(j + 1), color = colores[j], s = 20.0, edgecolors = 'black')
#     for h, centroide in enumerate(centroides):
#         x = centroide[0]
#         y = centroide[1]
#         plt.scatter(x, y, label = 'Centroide ' + str(h + 1), color = colores[h], s = 100.0, edgecolors = 'black')
#     plt.xlabel('Eje X')
#     plt.ylabel('Eje Y')
#     plt.xlim(limMinX, limMaxX)
#     plt.ylim(limMinY, limMaxY)
#     plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
#     plt.title('Iteración ' + str(i + 1) + '.\nEn esta iteración ' + str(cambiaron) + ' puntos cambiaron de clúster.\nCalinski-Harabasz score: ' + ("%.2f" % chScore))
#     plt.tight_layout()
#     plt.show(block = False)
# plt.show()