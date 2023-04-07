#importar dependencias necesarias para ejecutar qt
import sys # libreria que habilita funcionaliades del sistema
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from PyQt5.Qt import Qt
import serial

serial = serial.Serial('/dev/ttyUSB1', 115200)# (puerto, velocidad) objeto tipo serial
AcDe = True
#creacion de la clase principalll
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
        self.ui.label.setText(str(self.AcDe))
        if(self.AcDe):
            self.ui.ADusb.setText("Desactivar USB")
            self.prenderSerial()
        else:
            self.ui.ADusb.setText("Activar USB")
            self.apagarserial()
            
        self.AcDe = not self.AcDe#niego el estado de a variable activar desactivar
        #self.ui.label.setText(str(self.AcDe))#HAY UN HERROR cuando se llaman las funciones preder y apagar serial

    def prenderSerial(self):
        serial.open()
        
    def apagarserial(self):
        serial.close()

#Entrada por teclado      
    def keyPressEvent(self, event):
        #if int(event.key())== Qt.key_a: #este es un metodo mas sofisticado, pero implica un poco mas de trabajo
        if int(event.key())  == 65:#se preciono la a
            self.click_mex()
        elif int(event.key())  == 68:#se preciono la d
            self.click_max()
        elif int(event.key())  == 87:#se preciono la w
            self.click_may()
        elif int(event.key())  == 83:#"se preciono la s"
            self.click_mey()
        else:
            self.click_centrar()

#if que ejecuta, principal   
if __name__ == "__main__":
    app = QApplication(sys.argv)
    laberin = laberinto()
    laberin.show()
    sys.exit(app.exec())