import sys
from PyQt5 import uic, QtWidgets, QtCore
import Ventana_AgregarAlumno
import Ventana_AgregarParciales
import Ventana_VisualizarDatos
##########################################################################

qtCreatorFile1 = "Main_CalculaPromedioAlumnos.ui"  # Nombre del archivo aquí.
Ui_MainWindow1, QtBaseClass1 = uic.loadUiType(qtCreatorFile1)

class MyMainWindow(QtWidgets.QMainWindow, Ui_MainWindow1):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow1.__init__(self)
        self.setupUi(self)

        # Área de los Signals / Configuracion
        self.btn_agregar_alumno.clicked.connect(self.agregar_alumno)
        self.btn_agregar_parciales.clicked.connect(self.agregar_parciales)
        self.btn_guardar.clicked.connect(self.guardar)
        self.btn_visualizar.clicked.connect(self.visualizar)

        #Op1
        #self.lw_lista_alumnos.currentItemChanged.connect(self.cambia_usuario)
        #Op2
        self.lw_lista_alumnos.itemClicked.connect(self.cambia_usuario)

        self.datos_alumnos = [] #almacenara los datos de los alumnos
        self.usuario = None

    # Área de los Slots
    def agregar_alumno(self):
        # manda la referencia de la pantalla principal al dialog
        self.dialogo = Ventana_AgregarAlumno.MyDialog(self)

        self.dialogo.setModal(True)
        self.dialogo.show()

    def cambia_usuario(self):
        fila = self.lw_lista_alumnos.currentRow()
        print(fila)
        self.usuario = self.lw_lista_alumnos.currentItem().text()

    def agregar_parciales(self):
        if not self.usuario is None:
            print(self.usuario)
            # manda la referencia de la pantalla principal al dialog
            self.dialogo = Ventana_AgregarParciales.MyDialog(self)
            self.dialogo.txt_nombre.setText(self.usuario)
            self.dialogo.setModal(True)
            self.dialogo.show()

    def visualizar(self):
        self.dialogo = Ventana_VisualizarDatos.MyDialog()
        self.dialogo.setModal(True)
        self.dialogo.show()

    def guardar(self):
        archivo = open("respaldo_interno.sebas", "w")
        for alumno in self.datos_alumnos:
            
            archivo.write(alumno[0] + ",")
            for parcial in alumno[1]:
                archivo.write(str(parcial) + ",")
            archivo.write(str(alumno[2]))

            archivo.write("\n")
        archivo.flush()
        archivo.close()
        print("Archivo guardado")
##########################################################################


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
