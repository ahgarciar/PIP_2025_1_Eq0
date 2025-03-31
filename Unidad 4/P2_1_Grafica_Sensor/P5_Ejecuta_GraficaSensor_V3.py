import sys
from PyQt5 import uic, QtWidgets, QtGui, QtCore

import Plantilla_Grafica as gui
from matplotlib import pyplot as plt

import random as rnd

class MyApp(QtWidgets.QMainWindow, gui.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        gui.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.lecturas)
        self.btn_graficar.clicked.connect(self.graficar)

        self.x = [i for i in range(50)]
        self.y = []

    #Area de Slots
    def lecturas(self):

        while len(self.y) < len(self.x):
            t = rnd.randint(0, 1023)
            self.y.append(t)

        print(self.x)
        print(self.y)

        self.ax.plot(self.x, self.y)
        self.canvas.draw()

        plt.cla()
        del self.y[0]


    def graficar(self):
        self.segundoPlano.start(100)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

