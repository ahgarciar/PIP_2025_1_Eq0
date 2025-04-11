import sys
from PyQt5 import uic, QtWidgets, QtGui, QtCore
import serial as tarjeta

import Dialogo_ConexionArduino

qtCreatorFile = "P_Plantilla_Principal.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals


        self.arduino = None

        self.btn_iniciar.clicked.connect(self.iniciar)

        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.lecturas)

        self.bandera = 0
        self.datos = []

        #self.btn_led1.clicked.connect(self.control)
        #self.btn_led2.clicked.connect(self.control)
        #self.btn_led3.clicked.connect(self.control)

    # Área de los Slots
    def iniciar(self):
        self.dialogo = Dialogo_ConexionArduino.MyDialog(self)
        self.dialogo.setModal(True)
        self.dialogo.show()

    def control(self):
        obj = self.sender()
        texto = obj.text()
        led = obj.objectName()[-1]
        if self.arduino.isOpen():
            if texto == "PRENDER":
                obj.setText("APAGAR")
                c = led + "1"
                self.arduino.write(c.encode())
            else:
                obj.setText("PRENDER")
                c = led + "0"
                self.arduino.write(c.encode())


    def lecturas(self):
        if self.arduino.isOpen():
            if self.arduino.inWaiting(): #Serial.available()>0
                cadena = self.arduino.readline().decode().strip()
                if cadena != "":
                    self.datos.append(cadena)
                    if self.bandera == 0:
                        print(cadena)
                        ##PROCESAMIENTO DE LA CADENA....
                        cadena = cadena.split("-")
                        cadena = cadena[:-1]

                        cadena = [int(i) for i in cadena]
                        ######
                        self.lista_datos.addItem(str(cadena))
                        self.lista_datos.setCurrentRow(self.lista_datos.count()-1)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

