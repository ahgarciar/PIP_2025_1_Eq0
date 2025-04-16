import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P9_GetLineEditByName.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_ejecutar.clicked.connect(self.ejecutar)

    # Área de los Slots
    def ejecutar(self):
        nombreLineEdit = "txt_valor"

        txt = self.findChild(QtWidgets.QLineEdit, nombreLineEdit)

        txt.setText("VALOR")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

