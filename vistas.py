import PySimpleGUI as sg
import pyautogui
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from figuras import estadoInicial, figsKmeans
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
                ]]
    layout = [  [sg.Canvas(key='-CANVAS-')],
                [sg.Column(column, scrollable= False)],
                [sg.Button(button_text='Inicialización Aleatoria'),
                 sg.Button(button_text='Inicialización Heurística')]]

    window0 = sg.Window('Inicio', layout, finalize=True, element_justification='c')
    window  = [window0, None, None]
    active  = [True, False, False]
    event   = [None, None, None]
    values  = [None, None, None]
    canvas_elem = window[0]['-CANVAS-']
    canvas = canvas_elem.Widget
    fig_canvas_agg= None
    while True:              
        for i in range(3):
             if active[i] and window[i] != None:
                event[i], values[i] = window[i].read(timeout=50)
                if event[i] == sg.WIN_CLOSED or event[i] == 'Salir':
                    active[i] = False
                    window[i].close()
                    if i == 0:                        
                        break 
                elif event[i] == 'Abrir':
                    file_path = values[0]['file_path']
                    if file_path:
                        fig = estadoInicial(file_path)
                        if fig_canvas_agg != None:
                            fig_canvas_agg.get_tk_widget().pack_forget()  # Remove the previous figure
                        fig_canvas_agg = FigureCanvasTkAgg(fig, canvas)
                        fig_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)  
                        move_center(window[0])
                elif event[i] == 'Inicialización Aleatoria' and not active[1]: 
                    k_mapping = {'k2': 2, 'k3': 3, 'k4': 4, 'k5': 5}
                    selected_k_key = [key for key in k_mapping.keys() if values[0][key]][0]
                    selected_k = k_mapping[selected_k_key]
                    figInicial, figFinal, iteraciones = figsKmeans(values[0]['file_path'], selected_k, 'a')
                    layoutA = [  
                        [sg.Canvas(key='-figInicial-'),
                        sg.Canvas(key='-figFinal-')]
                    ]
                    window[1] =  sg.Window('Inicialización Aleatoria', layoutA, finalize=True, element_justification='c')                    
                    active[1] = True
                    canvas_elem_Inicial = window[1]['-figInicial-']
                    canvas_Inicial = canvas_elem_Inicial.Widget
                    fig_canvas_agg_inicial= FigureCanvasTkAgg(figInicial, canvas_Inicial)
                    fig_canvas_agg_inicial.get_tk_widget().pack(side='top', fill='both', expand=1)   
                    canvas_elem_Final = window[1]['-figFinal-']
                    canvas_Final = canvas_elem_Final.Widget
                    fig_canvas_agg_Final= FigureCanvasTkAgg(figFinal, canvas_Final)
                    fig_canvas_agg_Final.get_tk_widget().pack(side='top', fill='both', expand=1)    
                    move_center(window[1])
                elif event[i] == 'Inicialización Heurística' and not active[2]: 
                    k_mapping = {'k2': 2, 'k3': 3, 'k4': 4, 'k5': 5}
                    selected_k_key = [key for key in k_mapping.keys() if values[0][key]][0]
                    selected_k = k_mapping[selected_k_key]
                    figInicial, figFinal, iteraciones = figsKmeans(values[0]['file_path'], selected_k, 'h')
                    layoutH = [  
                        [sg.Canvas(key='-figInicial-'),
                        sg.Canvas(key='-figFinal-')]
                    ]
                    window[2] =  sg.Window('Inicialización Heurística', layoutH, finalize=True, element_justification='c')                    
                    active[2] = True
                    canvas_elem_Inicial = window[2]['-figInicial-']
                    canvas_Inicial = canvas_elem_Inicial.Widget
                    fig_canvas_agg_inicial= FigureCanvasTkAgg(figInicial, canvas_Inicial)
                    fig_canvas_agg_inicial.get_tk_widget().pack(side='top', fill='both', expand=1)   
                    canvas_elem_Final = window[2]['-figFinal-']
                    canvas_Final = canvas_elem_Final.Widget
                    fig_canvas_agg_Final= FigureCanvasTkAgg(figFinal, canvas_Final)
                    fig_canvas_agg_Final.get_tk_widget().pack(side='top', fill='both', expand=1)   
                    move_center(window[2])
        if i == 0 and active[i] == False:
         break
    window0.close()

def move_center(window):
    screen_width, screen_height = window.get_screen_dimensions()
    win_width, win_height = window.size
    x, y = (screen_width - win_width)//2, (screen_height - win_height)//4
    window.move(x, y)               
