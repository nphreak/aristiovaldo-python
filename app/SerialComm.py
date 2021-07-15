import serial


def serial_start():
    serialSetup = serial.Serial('COM6', 9600)
    return serialSetup

arduino = serial_start()

def send_data(data):    
    if(arduino.isOpen()):
        if(data == 1):
            arduino.write(b'1')
        elif(data == 0):
            arduino.write(b'0')
        elif(data == -1):
            arduino.close()
    else:
        print("erro")

