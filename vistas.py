import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

rutaArchivo = None
archivo = None

def cargarArchivo():
    global rutaArchivo, archivo
    ruta = filedialog.askopenfilename(filetypes = [('Archivos CSV', '*.csv')])
    nombre = os.path.basename(ruta)
    if ruta:
        btnMostrar.config(state = 'normal')
        rutaArchivo = ruta
        archivo = nombre

def mostrarValores():
    valor = spinbox.get()

    ventanaValores = tk.Toplevel(root)
    ventanaValores.title('Valores Seleccionados')

    etiquetaArchivo = ttk.Label(ventanaValores, text = f'Archivo Seleecionado: {archivo}')
    etiquetaArchivo.pack()

    etiquetaRutaArchivo = ttk.Label(ventanaValores, text = f'Ruta del Archivo Seleecionado: {rutaArchivo}')
    etiquetaRutaArchivo.pack()

    etiquetaValor = ttk.Label(ventanaValores, text = f'Valor Seleccionado: {valor}')
    etiquetaValor.pack()

root = tk.Tk()
root.title('TPI - IA 2 - Grupo 1')
root.resizable(False, False)

frame = ttk.Frame(root, padding = 5)
frame.grid()

tituloTP = ttk.Label(frame, text = 'Trabajo Práctico Integrador')
tituloTP.grid(column = 0, row = 0)

tituloCat = ttk.Label(frame, text = 'Inteligencia Artificial II - k-means')
tituloCat.grid(column = 0, row = 1)

btnDataset = ttk.Button(frame, text = 'Cargar Dataset (archivo .CSV)', command = cargarArchivo)
btnDataset.grid(column = 0, row = 2)

spinbox = ttk.Spinbox(frame, from_ = 2, to_ = 5)
spinbox.grid(column = 1, row = 2)
spinbox.set(5)

btnMostrar = ttk.Button(frame, text = 'Resolver', command = mostrarValores, state = 'disabled')
btnMostrar.grid(column = 0, row = 3)

root.mainloop()