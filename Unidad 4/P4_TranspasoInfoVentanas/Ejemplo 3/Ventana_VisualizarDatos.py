
from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile3 = "Ventana_VisualizarDatos.ui"  # Nombre del archivo aquí.
Ui_dialog, QtBaseClass3 = uic.loadUiType(qtCreatorFile3)


class MyDialog(QtWidgets.QDialog, Ui_dialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        Ui_dialog.__init__(self)
        self.setupUi(self)

        # Área de los Signals / Configuracion
        archivo = open("respaldo_interno.sebas")
        for fila in archivo:
            fila = fila.split(",")
            cadena = ("N:" + fila[0] +
                      " Parc.: " + fila[1] + "," + fila[2] + "," + fila[3] +
                      " Prom.:" + fila[4])
            self.lw_lista_alumnos.addItem(cadena)

    # Área de los Slots
