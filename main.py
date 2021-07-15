from app.SerialComm import send_data 
import PySimpleGUI as sg

layout = [[sg.Text("Hello from nPhreak")], [sg.Button("Liga")], [sg.Button("Desliga")], [sg.Button("Alternar", bind_return_key=True)], [sg.Button("OK")]]

window = sg.Window(title="O Falador App", layout=layout, margins=(200,100))
troca = "ligado"

while True:
    event, values = window.read()    
    if event == "Liga" :
        send_data(1)
    if event == "Desliga" :
        send_data(0)
    if event == "Alternar" :
        if troca == "ligado":
            send_data(0)
            troca = "desligado"
        elif troca == "desligado":
            send_data(1)
            troca = "ligado"
    if event == "OK" or event == sg.WIN_CLOSED:
        send_data(-1)
        break