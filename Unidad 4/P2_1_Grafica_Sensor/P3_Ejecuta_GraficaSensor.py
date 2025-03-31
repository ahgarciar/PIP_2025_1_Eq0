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
        x = [i for i in range(11)]
        y = [i+1 for i in x]
        print(x)
        print(y)

        self.ax.plot(x, y)
        self.canvas.draw()

    #Area de Slots

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

