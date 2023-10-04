import PySimpleGUI as sg
import pyautogui
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from figuras import estadoInicial


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
    layout = [[[sg.Canvas(key='-CANVAS-'),
                sg.Button(button_text = 'Dataset 1'),
                sg.Button(button_text = 'Dataset 2'),
                sg.Button(button_text = 'Dataset 3'),]],[
                   sg.Text(text = 'K =')
               ]]

    window = sg.Window('Inicio', layout, finalize=True)
    canvas_elem = window['-CANVAS-']
    canvas = canvas_elem.Widget
    fig = estadoInicial(1)
    print(fig)
    fig_canvas_agg = FigureCanvasTkAgg(fig, canvas)
    fig_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    while True:              
        event, values = window.read() 
        if event == sg.WIN_CLOSED or event == 'Salir':
            break      
        if event == 'Dataset 1':
            print('set1')
            fig = estadoInicial(1)
            fig_canvas_agg.get_tk_widget().pack_forget()  # Remove the previous figure
            fig_canvas_agg = FigureCanvasTkAgg(fig, canvas)
            fig_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1) 
        elif event == 'Dataset 2':
            print('set2')
            fig = estadoInicial(2)
            fig_canvas_agg.get_tk_widget().pack_forget()  # Remove the previous figure
            fig_canvas_agg = FigureCanvasTkAgg(fig, canvas)
            fig_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1) 
        elif event == 'Dataset 3':
            print('set3')
            fig = estadoInicial(3)         
            fig_canvas_agg.get_tk_widget().pack_forget()  # Remove the previous figure
            fig_canvas_agg = FigureCanvasTkAgg(fig, canvas)
            fig_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)          
    window.close()