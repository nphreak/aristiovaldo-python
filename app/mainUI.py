import PySimpleGUI as sg

def ui():
        
    layout = [[sg.Text("Hello from nPhreak")], [sg.Button("Liga")], [sg.Button("Desliga")]]

    window = sg.Window(title="O Falador App", layout=layout, margins=(200,100))
    return window
    
