from funciones import abrirCSV

import matplotlib.pyplot as plt

def estadoInicial(csv):
    puntos = abrirCSV(csv)
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
    ax.set_title('Estado inicial')
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
    fig.tight_layout()
    return fig

