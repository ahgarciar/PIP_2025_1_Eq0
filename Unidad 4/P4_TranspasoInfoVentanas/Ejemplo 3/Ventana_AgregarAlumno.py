
from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile3 = "Ventana_AgregarAlumno.ui"  # Nombre del archivo aquí.
Ui_dialog, QtBaseClass3 = uic.loadUiType(qtCreatorFile3)


class MyDialog(QtWidgets.QDialog, Ui_dialog):
    def __init__(self,  rPrincipal):
        QtWidgets.QDialog.__init__(self)
        Ui_dialog.__init__(self)
        self.setupUi(self)

        # Área de los Signals / Configuracion
        self.acceso = rPrincipal

        self.btn_agregar.clicked.connect(self.agregar)


    # Área de los Slots
    def agregar(self):
        try:
            nombre = self.txt_nombre.text()

            self.acceso.datos_alumnos.append([nombre, [], 0])
            self.acceso.lw_lista_alumnos.addItem(nombre)

            self.close()
        except Exception as error:
            print(error)
