import PySimpleGUI as sg

sg.theme('DefaultNoMoreNagging')  # Set the theme

layout = [
    [sg.Text('Select a CSV file')],
    [sg.InputText(key='file_path'), sg.FileBrowse(file_types=(("CSV Files", "*.csv"),))],
    [sg.Button('Open'), sg.Button('Exit')]
]

window = sg.Window('CSV File Selector', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'Open':
        file_path = values['file_path']
        if file_path:
            # You can now use the 'file_path' variable to work with the selected CSV file
            print(f'Selected CSV file: {file_path}')

window.close()