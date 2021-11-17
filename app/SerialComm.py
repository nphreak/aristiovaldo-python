from serial.tools import list_ports
import serial
import os


def list_all_ports():    
    com_port_list = list(list_ports.comports())
    port_name_list = []

    if len(com_port_list) > 0:
        for port in com_port_list:
            port_name_list.append(port.device)

    return port_name_list

def send_command():
    print("em construção")
