import PySimpleGUI as sg
import pyautogui
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from figuras import estadoInicial
import os


def getScreenSize():
     width, height= pyautogui.size()
     return width, height

def draw_figure(canvas, figure):
   tkcanvas = FigureCanvasTkAgg(figure, canvas)
   tkcanvas.draw()
   tkcanvas.get_tk_widget().pack(side='top', fill='both', expand=1)
   return tkcanvas

def call_vistas():
    sg.theme('DarkGrey2')
    sg.set_options(font=("Calibri", 14))
    window = make_main()
    while True:              
        event, values = window.read() 
        if event == sg.WIN_CLOSED or event == 'Salir':
            break      
        if event == 'Iniciar':
            window.close()
            make_inicio()            
        window.close()

def make_main():    
    srcAncho, srcAlto = getScreenSize()   
    layout = [[sg.Text(text = 'Trabajo Práctico Integrador',
                   font=('Calibri', 30),
                   size= 30, 
                   expand_x= True,
                   justification= 'center')],     
            [sg.Text(text = 'Universidad Gastón Dachary - Inteligencia Artificial II - 2023', 
                    font=('Calibri', 15),
                    size= 15, 
                    expand_x= True,
                    justification= 'center')], 
            [sg.Text(' ')],  
            [sg.Text(text = 'Análisis del Algoritmo k-means',   
                    font=('Calibri', 20),
                    size= 20, 
                    expand_x= True,
                    justification= 'center')], 
            [sg.Text(' ')],  
            [sg.Button(button_text='Iniciar',
                        size=(15,2), font=('Calibri')), 
                        sg.Button(button_text='Salir',
                                size=(15,2), font=('Calibri'))],
            [sg.Text(' ')],  
            [sg.Text(text = 'Malazotto, Soledad - Mezio, Santiago - Suárez, Guillermo',
                    font=('Calibri', 10),
                    size= 10, 
                    expand_x= True,
                    justification= 'center')]]
    return sg.Window('TPI Inteligencia Artificial II', layout, element_justification='c', size=(650, 400))      

def make_inicio():  
    current_folder = os.getcwd()
    column =[   [
                    sg.Text('Seleccionar un archivo CSV'),
                    sg.InputText(key='file_path'), sg.FileBrowse('Buscar',initial_folder=current_folder+'/Datasets', file_types=(("CSV Files", "*.csv"),)), 
                    sg.Button(button_text='Abrir')                   
                ],
                [
                    sg.Text(text = 'K ='),
                    sg.Radio('2', 'k', key='k2', default=True),
                    sg.Radio('3', 'k', key='k3', default=False),
                    sg.Radio('4', 'k', key='k4', default=False),
                    sg.Radio('5', 'k', key='k5', default=False)
                ],
                [
                    sg.Text(text='Inicialización:'),
                    sg.Radio('Aleatoria', 'inicio', key='iA', default=True),
                    sg.Radio('Heurística', 'inicio', key='iH', default=False)
                ]]
    layout = [[sg.Canvas(key='-CANVAS-'),
               sg.Column(column, scrollable= False),
               ],
               [sg.Button(button_text='Iniciar')]]

    window0 = sg.Window('Inicio', layout, finalize=True, element_justification='c')
    window  = [window0, None]
    active  = [True, False]
    event   = [None, None]
    values  = [None, None]
    canvas_elem = window[0]['-CANVAS-']
    canvas = canvas_elem.Widget
    fig_canvas_agg= None
    while True:              
        for i in range(2):
             if active[i] and window[i] != None:
                event[i], values[i] = window[i].read(timeout=50)
                if event[i] == sg.WIN_CLOSED or event[i] == 'Salir':
                    if i == 0:
                        active[i] = False
                        window[i].close()
                        break      
                
                elif event[i] == 'Abrir':
                    file_path = values['file_path']
                    if file_path:
                        fig = estadoInicial(file_path)
                        if fig_canvas_agg != None:
                            fig_canvas_agg.get_tk_widget().pack_forget()  # Remove the previous figure
                        fig_canvas_agg = FigureCanvasTkAgg(fig, canvas)
                        fig_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)         
                elif event[i] == 'Iniciar': 
                    k_mapping = {'k2': 2, 'k3': 3, 'k4': 4, 'k5': 5}
                    selected_k_key = [key for key in k_mapping.keys() if values[0][key]][0]
                    selected_k = k_mapping[selected_k_key]
                    inicializacion_mapping = {'iA': 'Aleatoria', 'iH': 'Heurística'}
                    selected_inicializacion_key = [key for key in inicializacion_mapping.keys() if values[0][key]][0]
                    selected_inicializacion = inicializacion_mapping[selected_inicializacion_key]
                    
                    print(f'Selected K: {selected_k}')
                    print(f'Selected Inicialización: {selected_inicializacion}')