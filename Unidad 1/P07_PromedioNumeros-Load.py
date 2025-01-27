import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P07_PromedioNumeros-Load.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.btn_cargar.clicked.connect(self.cargar)
        self.btn_agregar.clicked.connect(self.agregar)
        self.btn_guardar.clicked.connect(self.guardar)
        self.calificaciones = []

    # Área de los Slots
    def cargar(self):
        ##TAREA EJ 10 ---. COMO COMPRUEBO SI EL ARCHIVO EXISTE ? ....
        archivo = open("../Archivos/calificaciones.csv")
        contenido = archivo.readlines()
        print(contenido)
        datos = [int(x) for x in contenido]
        print(datos)
        ##TAREA EJ 11 --- EN LUGAR DE SOBREESCRIBIR, CONCATENAR :D!
        self.calificaciones = datos
        self.promedio()
        #TAREA EJ 12.--- ASEGURARSE DE QUE SOLO SE PUEDA CARGAR HASTA ANTES DE
        # AGREGAR LA PRIMERA CALIFICACION ... ---> ENABLES Y/O CODIGO

    def agregar(self):
        calificacion = int(self.txt_calificacion.text())
        self.calificaciones.append(calificacion)
        self.promedio()

    def promedio(self):
        prom = sum(self.calificaciones) / len(self.calificaciones)
        self.txt_promedio.setText(str(prom))

    def guardar(self):
        archivo = open("../Archivos/calificaciones.csv", "w") # w = write  --- a = append
        for c in self.calificaciones:
            archivo.write(str(c) + "\n")
        archivo.flush()
        archivo.close()
        self.msj("Archivo Guardado con Exito!")

    def msj(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

