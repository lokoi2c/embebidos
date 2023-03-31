#importar dependencias necesarias para ejecutar qt
import sys # libreria que habilita funcionaliades del sistema
from PyQt5.QtWidgets import (QApplication, QWidget,QLayout, QGridLayout, QLabel, QPushButton)

#funcion llamada (slot) cuando se hace click
def click():
    print('entrada a facevook')
    label.setText('No te espiamos, ok')#cambiar texto al objeto label
    
if __name__ == "__main__": #definicion definida del main principal
    #lineas para ejecutar la interraz grafica
    app = QApplication(sys.argv) #objeto de tipo Qt

    #creacion de objetos
    windows = QWidget()
    boton = QPushButton('ok')
    label = QLabel('FaceVook')
    bienvenida = QLabel('Bienvenido a FaceVook')
    layout = QGridLayout()
    
    #objeto conectado a una señal (slot)
    boton.clicked.connect(click)

    #posicon en pamntalla
    layout.addWidget(bienvenida, 0,2)
    layout.addWidget(label, 1,0)
    layout.addWidget(boton, 1,2)


    windows.setLayout(layout)
    windows.show()
    sys.exit(app.exec())