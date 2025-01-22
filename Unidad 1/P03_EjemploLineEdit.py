import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P03_EjemploLineEdit.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.btn_saludar.clicked.connect(self.saludar)

    # Área de los Slots
    def saludar(self):
        cadena = self.txt_nombre.text()  # str
        if cadena!= "":
            self.msj("Hola " + cadena +", buen día! :D!")
        else:
            self.msj("Debes ingresar tu nombre para continuar")

    def msj(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

