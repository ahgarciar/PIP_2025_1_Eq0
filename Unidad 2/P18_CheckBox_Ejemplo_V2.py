import time as t
import sys
from PyQt5 import uic, QtWidgets, QtCore
qtCreatorFile = "P17_CheckBox.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.cb_dormir.clicked.connect(self.control)
        self.cb_cine.toggled.connect(self.control)

    # Área de los Slots
    def control(self):
        obj = self.sender()  #.objectName()
        valor = obj.isChecked()
        print("Objeto ", obj.text(), ": ", valor)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

