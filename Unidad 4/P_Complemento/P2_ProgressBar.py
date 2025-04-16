import sys
from PyQt5 import uic, QtWidgets, QtCore
qtCreatorFile = "P2_progressBar.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(0)

        self.progressBar.valueChanged.connect(self.cambiaValor)
        self.txt_valor.setText("0")

        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.actualiza)

        self.contador = 0
        self.segundoPlano.start(150)

    # Área de los Slots

    def actualiza(self):
        self.contador+=1
        self.progressBar.setValue(self.contador)
        if self.contador==100:
            self.segundoPlano.stop()


    def cambiaValor(self):
        self.txt_valor.setText(str(self.progressBar.value()))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

