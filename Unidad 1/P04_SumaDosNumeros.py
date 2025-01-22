import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P04_SumaDosNumeros.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.btn_sumar.clicked.connect(self.sumar)

    # Área de los Slots
    def sumar(self):
        try:
            a = float(self.txt_A.text())
            b = float(self.txt_B.text())
            r = a+b
            self.msj("La suma es: " + str(r))
        except Exception as error:
            print(error)


    def msj(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

