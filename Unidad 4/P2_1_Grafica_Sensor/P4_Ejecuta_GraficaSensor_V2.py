import sys
from PyQt5 import uic, QtWidgets, QtGui

import Plantilla_Grafica as gui
from matplotlib import pyplot as plt

class MyApp(QtWidgets.QMainWindow, gui.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        gui.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_graficar.clicked.connect(self.graficar)

    #Area de Slots
    def graficar(self):
        x = [i for i in range(10)]

        import random as rnd
        y = []
        for i in x:
            t = rnd.randint(0, 1023)
            y.append(t)

        print(x)
        print(y)

        self.ax.plot(x, y)
        self.canvas.draw()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

