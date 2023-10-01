import kmeans as k_means
import funciones as funciones_tp

def ch_score():
    #Permite calcular el indice Calinski-Harabasz
    cant_pruebas = 2
    puntos = funciones_tp.abrirCSV('Datasets/dataset_1.csv')
    cant_puntos = len(puntos)
    #print("Cantidad de puntos: " + str(cant_puntos))
    #se prueba en todo el rango de los k posibles
    for k in range(2,6):
        ch_score_promedio = 0
        #print("Para k = " + str(k))
        for i in range(cant_pruebas):
            #print("Prueba " + str(i))
            bgss_prueba_i = 0
            wgss_prueba_i = 0
            ch_score_prueba_i = 0
            centroides, puntos = k_means.marcarCentroidesAleatorios(k, puntos)
            iteraciones = k_means.kMeans(k, puntos, centroides)
            #Se utiliza solamente la iteración final, por eso el [-1]
            #UI: siglas para última iteración
            centroides_UI = iteraciones[-1][0]
            clusters_UI = iteraciones[-1][1]
            bgss_prueba_i = bgss(puntos, centroides_UI, clusters_UI)
            wgss_prueba_i = wgss(centroides_UI, clusters_UI)
            ch_score_prueba_i = ((bgss_prueba_i/wgss_prueba_i) * ((cant_puntos - k)/(k-1)))
            ch_score_promedio +=  ch_score_prueba_i
            # print("BGSS = " + str(bgss_prueba_i))
            # print("WGSS = " + str(wgss_prueba_i))
            # print("Diferencia: " + str(bgss_prueba_i - wgss_prueba_i))
            # print("CH de la prueba " + str(ch_score_prueba_i))
        ch_score_promedio /= cant_pruebas 
        print("Para k = " + str(k) + " se obtuvo un CH promedio de " + str(ch_score_promedio))
        #print("----------------------------")

def bgss(dataset, centroides, clusters):
    #Función que devuelve la dispersión inter-cluster
    #El baricentro se refiere al centroide del dataset
    sumatoria = 0
    cant_puntos = 0
    distancia_baricentro = 0
    baricentro = funciones_tp.actualizarCentroide(dataset, 0)
    for i, cluster in enumerate(clusters):
        cant_puntos = len(cluster)
        distancia_baricentro = funciones_tp.calcularDistancia(centroides[i], baricentro)
        sumatoria += (cant_puntos * distancia_baricentro)
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

ch_score()