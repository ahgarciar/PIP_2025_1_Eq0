
from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile3 = "Ventana_CalcularPromedio.ui"  # Nombre del archivo aquí.
Ui_dialog, QtBaseClass3 = uic.loadUiType(qtCreatorFile3)


class MyDialog(QtWidgets.QDialog, Ui_dialog):
    def __init__(self,  rPrincipal):
        QtWidgets.QDialog.__init__(self)
        Ui_dialog.__init__(self)
        self.setupUi(self)

        # Área de los Signals / Configuracion
        self.acceso = rPrincipal

        self.btn_calcular.clicked.connect(self.calcular)


    # Área de los Slots
    def calcular(self):
        try:
            parcial1 = int(self.txt_parcial1.text())
            parcial2 = int(self.txt_parcial2.text())
            parcial3 = int(self.txt_parcial3.text())

            promedio = (parcial1 + parcial2 + parcial3) / 3
            promedio = round(promedio, 2)

            indice = self.acceso.lw_lista_alumnos.currentRow()

            self.acceso.datos_alumnos[indice][1] = [parcial1, parcial2, parcial3]
            self.acceso.datos_alumnos[indice][2] = promedio

            self.close()
        except Exception as error:
            print(error)
