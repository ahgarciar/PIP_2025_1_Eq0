import sys
from PyQt5 import uic, QtWidgets, QtGui, QtCore
import serial as tarjeta

qtCreatorFile = "P41_ArduinoPythonGUI_ReadWrite_VariosSensores.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.txt_com.setText("/dev/cu.usbmodem1301")

        self.arduino = None

        self.btn_accion.clicked.connect(self.accion)

        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.lecturas)

        self.bandera = 0
        self.datos = []

        self.btn_control.clicked.connect(self.control)

    # Área de los Slots
    def control(self):
        texto = self.btn_control.text()
        if self.arduino.isOpen:
            if texto == "PRENDER":
                self.btn_control.setText("APAGAR")
                self.arduino.write("1".encode())
            else:
                self.btn_control.setText("PRENDER")
                self.arduino.write("0".encode())


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

    def accion(self):
        try:
            texto = self.btn_accion.text()
            com = self.txt_com.text()
            if texto == "CONECTAR":
                self.arduino = tarjeta.Serial(com, baudrate=9600, timeout= 1)
                self.segundoPlano.start(100)
                self.btn_accion.setText("DESCONECTAR")
                self.txt_estado.setText("CONECTADO")
            elif texto == "DESCONECTAR":
                self.segundoPlano.stop()
                self.arduino.close()
                self.btn_accion.setText("RECONECTAR")
                self.txt_estado.setText("DESCONECTADO")
            elif texto == "RECONECTAR":
                self.arduino.open()
                self.segundoPlano.start(100)
                self.btn_accion.setText("DESCONECTAR")
                self.txt_estado.setText("RECONECTADO")
        except Exception as error:
            print(error)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

