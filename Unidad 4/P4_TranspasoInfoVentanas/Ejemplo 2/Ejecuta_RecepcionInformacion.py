import sys
from PyQt5 import uic, QtWidgets, QtCore
import VentanaSecundaria
##########################################################################

qtCreatorFile1 = "Main_RecepcionInfo.ui"  # Nombre del archivo aquí.
Ui_MainWindow1, QtBaseClass1 = uic.loadUiType(qtCreatorFile1)

class MyMainWindow(QtWidgets.QMainWindow, Ui_MainWindow1):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow1.__init__(self)
        self.setupUi(self)

        # Área de los Signals / Configuracion
        self.btn_sumar.clicked.connect(self.sumar)

    # Área de los Slots
    def sumar(self):
        # manda la referencia de la pantalla principal al dialog
        self.dialogo = VentanaSecundaria.MyDialog(self)

        self.dialogo.setModal(True)
        self.dialogo.show()

##########################################################################


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
