import time as t
import sys
from PyQt5 import uic, QtWidgets, QtCore
qtCreatorFile = "P12_RadioButton_GroupBox.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.rb_perro.clicked.connect(self.perro)
        self.rb_gato.clicked.connect(self.gato)
        self.rb_hamster.clicked.connect(self.hamster)

        self.rb_negro.toggled.connect(self.negro)
        self.rb_rojo.toggled.connect(self.rojo)
        self.rb_azul.toggled.connect(self.azul)

    # Área de los Slots
    def perro(self):
        print("Perro")
    def gato(self):
        print("Gato")
    def hamster(self):
        print("Hamster")

    def negro(self):
        v = self.rb_negro.isChecked()
        print("Negro", v)
    def rojo(self):
        v = self.rb_rojo.isChecked()
        print("Rojo", v)
    def azul(self):
        v = self.rb_azul.isChecked()
        print("Azul", v)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

