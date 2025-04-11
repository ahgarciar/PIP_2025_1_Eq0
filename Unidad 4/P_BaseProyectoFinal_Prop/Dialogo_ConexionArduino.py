import sys
from PyQt5 import uic, QtWidgets, QtCore

import serial as tarjeta

qtCreatorFile3 = "Dialogo_ConexionArduino.ui"  # Nombre del archivo aquí.
Ui_dialog, QtBaseClass3 = uic.loadUiType(qtCreatorFile3)

class MyDialog(QtWidgets.QDialog, Ui_dialog):
    def __init__(self, referencia_a_main):
        QtWidgets.QDialog.__init__(self)
        Ui_dialog.__init__(self)
        self.setupUi(self)

        # Área de los Signals / Configuracion
        self.txt_com.setText("/dev/cu.usbmodem21201")
        self.btn_accion.clicked.connect(self.accion)

        self.principal = referencia_a_main

    # Área de los Slots
    def accion(self):
        try:
            texto = self.btn_accion.text()
            com = self.txt_com.text()
            if texto == "CONECTAR":
                self.principal.arduino = tarjeta.Serial(com, baudrate=9600, timeout=1)
                self.principal.segundoPlano.start(100)
                self.btn_accion.setText("DESCONECTAR")
                self.principal.txt_estado.setText("CONECTADO")
            elif texto == "DESCONECTAR":
                self.principal.segundoPlano.stop()
                self.principal.arduino.close()
                self.btn_accion.setText("RECONECTAR")
                self.principal.txt_estado.setText("DESCONECTADO")
            elif texto == "RECONECTAR":
                self.principal.arduino.open()
                self.principal.segundoPlano.start(100)
                self.btn_accion.setText("DESCONECTAR")
                self.principal.txt_estado.setText("RECONECTADO")
        except Exception as error:
            print(error)
