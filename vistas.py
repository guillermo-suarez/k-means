import PySimpleGUI as sg
import pyautogui
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from figuras import estadoInicial, figsKmeans, figIteracionKmeans
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
    csv_insertado = False
    column =[   [
                    sg.Text('Seleccionar un archivo CSV'),
                    sg.InputText(key='file_path'), sg.FileBrowse('Buscar',initial_folder=current_folder+'/Datasets', file_types=(("Archivos CSV", "*.csv"),)), 
                    sg.Button(button_text='Previsualizar')                   
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
                [sg.Button(button_text='Inicialización Aleatoria', key='Aleatoria', disabled=not csv_insertado),
                 sg.Button(button_text='Inicialización Heurística', key='Heuristica', disabled=not csv_insertado)]]

    window0 = sg.Window('Inicio', layout, finalize=True, element_justification='c')
    window  = [window0, None, None, None, None]
    active  = [True, False, False, False, False]
    event   = [None, None, None, None, None]
    values  = [None, None, None, None, None]
    canvas_elem = window[0]['-CANVAS-']
    canvas = canvas_elem.Widget
    fig_canvas_agg= None
    while True:              
        for i in range(5):
             if active[i] and window[i] != None:
                event[i], values[i] = window[i].read(timeout=50)
                if(event[i] != "__TIMEOUT__"):
                    print(i)
                    print(event[i])
                if event[i] == sg.WIN_CLOSED or event[i] == 'Salir':
                    active[i] = False
                    window[i].close()
                    if i == 0:                        
                        break 
                elif event[i] == 'Previsualizar':
                    file_path = values[0]['file_path']
                    if file_path:
                        fig = estadoInicial(file_path)
                        if fig_canvas_agg != None:
                            fig_canvas_agg.get_tk_widget().pack_forget()  # Remove the previous figure
                        fig_canvas_agg = FigureCanvasTkAgg(fig, canvas)
                        fig_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)  
                        move_center(window[0])
                        csv_insertado = True
                        window0['Aleatoria'].update(disabled=False)
                        window0['Heuristica'].update(disabled=False)
                elif event[i] == 'Aleatoria' and not active[1]: 
                    k_mapping = {'k2': 2, 'k3': 3, 'k4': 4, 'k5': 5}
                    selected_k_key = [key for key in k_mapping.keys() if values[0][key]][0]
                    selected_k = k_mapping[selected_k_key]
                    figInicial, figFinal, iteracionesA, kUsado, puntosUsados = figsKmeans(values[0]['file_path'], selected_k, 'a')
                    layoutA = [  
                        [sg.Canvas(key='-figInicial-'),
                        sg.Canvas(key='-figFinal-')],
                        [sg.Button(button_text="Ver Iteraciones")]
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
                elif event[i] == 'Heuristica' and not active[2]: 
                    k_mapping = {'k2': 2, 'k3': 3, 'k4': 4, 'k5': 5}
                    selected_k_key = [key for key in k_mapping.keys() if values[0][key]][0]
                    selected_k = k_mapping[selected_k_key]
                    figInicial, figFinal, iteracionesH, kUsado, puntosUsados = figsKmeans(values[0]['file_path'], selected_k, 'h')
                    layoutH = [  
                        [sg.Canvas(key='-figInicial-'),
                        sg.Canvas(key='-figFinal-')],
                        [sg.Button(button_text="Ver Iteraciones")]
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
                elif event[i] == "Ver Iteraciones":
                    if i == 1:
                        layoutIter = make_iteraciones(iteracionesA, "IterAleatorio")                        
                        window[3] =  sg.Window('Iteraciones con Inicialización Aleatoria', layoutIter, finalize=True, element_justification='c') 
                        active[3] = True   
                        canvas_elem_iterA = window[3]['-figIteracion-']
                        canvas_iterA = canvas_elem_iterA.Widget
                        fig_canvas_agg_iterA= None
                    elif i == 2:
                        layoutIter = make_iteraciones(iteracionesH, "IterHeuristico")
                        window[4] =  sg.Window('Iteraciones con Inicialización Heurística', layoutIter, finalize=True, element_justification='c')     
                        active[4] = True
                        canvas_elem_iterH = window[4]['-figIteracion-']
                        canvas_iterH = canvas_elem_iterH.Widget
                        fig_canvas_agg_iterH= None
                elif event[i] == "IterAleatorio":                    
                    clicked_row_index = values[i][event[i]][0]
                    if fig_canvas_agg_iterA != None:
                            fig_canvas_agg_iterA.get_tk_widget().pack_forget()
                    figIter = figIteracionKmeans(puntosUsados, iteracionesA, kUsado, clicked_row_index)                    
                    fig_canvas_agg_iterA= FigureCanvasTkAgg(figIter, canvas_iterA)                    
                    fig_canvas_agg_iterA.get_tk_widget().pack(side='top', fill='both', expand=1)
                elif event[i] == "IterHeuristico":
                    clicked_row_index = values[i][event[i]][0]   
                    if fig_canvas_agg_iterH != None:
                            fig_canvas_agg_iterH.get_tk_widget().pack_forget()
                    figIter = figIteracionKmeans(puntosUsados, iteracionesH, kUsado, clicked_row_index)                    
                    fig_canvas_agg_iterH= FigureCanvasTkAgg(figIter, canvas_iterH)                    
                    fig_canvas_agg_iterH.get_tk_widget().pack(side='top', fill='both', expand=1)

        if i == 0 and active[i] == False:
         break
    window0.close()

def move_center(window):
    screen_width, screen_height = window.get_screen_dimensions()
    win_width, win_height = window.size
    x, y = (screen_width - win_width)//2, (screen_height - win_height)//4
    window.move(x, y)               

def make_iteraciones(iteraciones, tipo):
    filas = len(iteraciones)
    columnas = 1
    valores = []
    cabeceras = ["Iteraciones"]
    for i, iter in enumerate(iteraciones):
        fila = ["Iteración " + str(i)]
        valores.append(fila)
    column=[[sg.Canvas(key='-figIteracion-')]]
    layout = [[sg.Column(column, scrollable= False),
              [sg.Text(text='Iteraciones', font=('Calibri', 30), 
               justification= 'center')],                
               sg.Table(values = valores, 
                         headings = cabeceras,
                         vertical_scroll_only = False,
                         enable_events = True,
                         key=tipo,
                         expand_x=True,
                         expand_y=True,
                         justification= 'center',
                         auto_size_columns=True,
                         col_widths=6)]                
                ]
    return layout