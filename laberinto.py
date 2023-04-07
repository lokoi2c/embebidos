#importar dependencias necesarias para ejecutar qt
import sys # libreria que habilita funcionaliades del sistema
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
import serial

serial = serial.Serial('/dev/ttyUSB0', 115200)# (puerto, velocidad) objeto tipo serial

#creacion de la clase principal
class laberinto(QMainWindow):#herencia
    def __init__(self):
        super().__init__()#(laberinto, self).__init__()
        self.ui = uic.loadUi('interfaz_qt.ui', self)#otro change
        
        #eventos asociados a una funcion, llevan nombre del boton  y la funcion a ejecutar
        self.ui.max.clicked.connect(self.click_max)
        self.ui.mex.clicked.connect(self.click_mex)#shit
        self.ui.may.clicked.connect(self.click_may)#otro cambio
        
        self.ui.mey.clicked.connect(self.click_mey)#ojala sirva
        self.ui.centro.clicked.connect(self.click_centrar)
        self.ui.ADusb.clicked.connect(self.click_AcDeUSB) #ADusb traduccion:ActivarDesactivar_usb
        
        self.AcDe = True
        
    def click_max(self):
        serial.write(b'd')
            
    def click_mex(self):
        serial.write(b'a')
        
    def click_may(self):
        serial.write(b'w')
        
    def click_mey(self):
        serial.write(b's')
        
    def click_centrar(self):
        serial.write(b'e')
    
    def click_AcDeUSB(self):
        if(self.AcDe):
            self.prenderSerial()
            self.ui.ADusb.setText("Desactivar USB")
        else:
            self.apagarserial()
            self.ui.ADusb.setText("Activar USB")
            
        self.AcDe = ~self.AcDe#niego es estado de a variable activar desactivar

    def prenderSerial(self):
        serial.open()
        
    def apagarserial(self):
        serial.close()
        

#if que ejecuta, principal   
if __name__ == "__main__":
    app = QApplication(sys.argv)
    laberin = laberinto()
    laberin.show()
    sys.exit(app.exec())