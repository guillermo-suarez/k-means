import kmeans as k_means
import funciones as funciones_tp

def ch_score():
    #Permite calcular el indice Calinski-Harabasz
    cant_pruebas = 0
    puntos = funciones_tp.abrirCSV('Datasets/dataset_2.csv')
    total_observaciones = len(puntos)
    #se prueba en todo el rango de los k posibles
    for k in range(1,6):
        ch_score_promedio = 0
        for i in range(cant_pruebas):
            centroides, puntos = k_means.marcarCentroidesAleatorios(k, puntos)
            iteraciones = k_means.kMeans(k, puntos, centroides)
            #Se utiliza solamente la iteración final
            centroides_ultima_iteracion = iteraciones[-1][0]
            clusters = iteraciones[-1][1]

def bgss(dataset, centroides, clusters):
    #Función que devuelve la dispersión inter-cluster
    centroide_dataset = funciones_tp.actualizarCentroide(dataset,0)
    sumatoria = 0
    for i, cluster in enumerate(clusters):
        sumatoria += (len(cluster) * funciones_tp.calcularDistancia(centroides[i],centroide_dataset))
    return sumatoria

def wgss(centroides, clusters):
    #Función que devuelve la dispersión intra-cluster
    sumatoria_total = 0
    for i, cluster in enumerate(clusters):
        sumatoria = 0
        for punto in cluster:
            sumatoria += funciones_tp.calcularDistancia(centroides[i], punto)
        sumatoria_total += sumatoria
    return sumatoria_total
