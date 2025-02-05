import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P09_SliderImagenes_Manual.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.selectorImagen.setMinimum(1)
        self.selectorImagen.setMaximum(3)
        self.selectorImagen.setSingleStep(1)
        self.selectorImagen.setValue(1) ##valr inicial
        self.selectorImagen.valueChanged.connect(self.cambiaValor)

        self.diccionarioDatos = {
            1: (":/Ejercicios/ImagenGatoEuropeo.png",["Gato", "4 meses", "Raton"]),
            2: (":/Logos/FIT_logo_vertical.png", ["Castor", "65 años", "Estudiar"]),
            3: (":/Logos/log_uat_nuevo.png", ["Correcaminos", "75 años", "Superacion"])
        }
        self.indice = 1
        self.obtenerDatos()

    # Área de los Slots
    def obtenerDatos(self):
        nombre = self.diccionarioDatos[self.indice][1][0]
        edad = self.diccionarioDatos[self.indice][1][1]
        juguete = self.diccionarioDatos[self.indice][1][2]
        self.txt_nombre.setText(nombre)
        self.txt_edad.setText(edad)
        self.txt_juguete.setText(juguete)

        self.imagen_descripcion.setPixmap(QtGui.QPixmap(
            self.diccionarioDatos[self.indice][0]))

    def cambiaValor(self):
        self.indice = self.selectorImagen.value()
        self.obtenerDatos()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

