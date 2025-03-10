import sys
from PyQt5 import uic, QtWidgets
#qtCreatorFile = "P0_Plantilla.ui"  # Nombre del archivo aquí.
#Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

import P1_vPython_Ejemplo as interfaz #import el modulo que tiene la clase con la interfaz convertida

class MyApp(QtWidgets.QMainWindow, interfaz.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        interfaz.Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        #self.btn_sumar.
        self.btn_sumar.clicked.connect(self.sumar)

    # Área de los Slots
    def sumar(self):
        a = int(self.txt_num1.text())
        b = int(self.txt_num2.text())
        r = a+b
        self.mensaje("La suma es: " + str(r))

    def mensaje(self, msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

