import sys
import os

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QObject, Slot, Signal

from app.SerialComm import list_all_ports

class MainWindow(QObject):
    def __init__(self):
        QObject.__init__(self)
        
    setPortList = Signal(str)
    connectToSerialPort = Signal(str)
    disconnectSerialPort = Signal(str)
    
    
    @Slot(str)
    def port_list(self, name):
        ports = list_all_ports()
        for port in ports:
            name = name + ", " + port
        self.setPortList.emit(name)
    
    @Slot(str)
    def connect(self, selected_port):
        self.connectToSerialPort.emit("Connected to arduino on port " + selected_port)
    
    @Slot(str)
    def disconnect(self, selected_port):
        self.disconnectSerialPort.emit("Serial Comm closed")

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    
    # Get Context
    main = MainWindow()
    engine.rootContext().setContextProperty("backend", main)
    
    # Load QML file
    engine.load(os.path.join(os.path.dirname(__file__), "app/qml/main.qml"))

    #caso de erro
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())