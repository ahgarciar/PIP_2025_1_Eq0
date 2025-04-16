from QLabelClickeable import clickable

import sys
from PyQt5 import uic, QtWidgets, QtCore, QtGui
qtCreatorFile = "P8_Memorama.ui"  # Nombre del archivo
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #EJEMPLO NO TERMINADO

        clickable(self.img1).connect(self.clicImage1)
        clickable(self.img2).connect(self.clicImage2)
        clickable(self.img3).connect(self.clicImage3)
        clickable(self.img4).connect(self.clicImage4)

        self.listaImagenesDisponibles = [
            [0, ":/Logos/FIT_logo_vertical.png"],
            [1, ":/Logos/log_uat_nuevo.png"],
        ]

        self.contMax = 2
        self.ordenImagenesMemorama = [];
        self.estadoTarjetas = [] #determina si la tarjeta se puede voltear o no...
        for i in self.listaImagenesDisponibles:
            for j in range(self.contMax):
                self.ordenImagenesMemorama.append(i[0])
                self.estadoTarjetas.append(True)

        #print(ordenImagenesMemorama)

        import random as rnd
        rnd.shuffle(self.ordenImagenesMemorama)
        print(self.ordenImagenesMemorama)

        self.btn_validar.clicked.connect(self.validar)

        self.tajetasVolteadas = 0

    def mensajeEmergente(self, msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()

    def clicImage1(self):
        #self.mensajeEmergente("imagen 1")
        if self.estadoTarjetas[0] and self.tajetasVolteadas<self.contMax:
            self.img1.setPixmap(QtGui.QPixmap(
                self.listaImagenesDisponibles[self.ordenImagenesMemorama[0]][1]
            ))
            self.tajetasVolteadas += 1
            self.estadoTarjetas[0] = False

    def clicImage2(self):
        if self.tajetasVolteadas < self.contMax:
            #self.mensajeEmergente("imagen 2")
            self.img2.setPixmap(QtGui.QPixmap(
                self.listaImagenesDisponibles[self.ordenImagenesMemorama[1]][1]
            ))
            self.tajetasVolteadas += 1

    def clicImage3(self):
        if self.tajetasVolteadas < self.contMax:
            #self.mensajeEmergente("imagen 3")
            self.img3.setPixmap(QtGui.QPixmap(
                self.listaImagenesDisponibles[self.ordenImagenesMemorama[2]][1]
            ))
            self.tajetasVolteadas += 1

    def clicImage4(self):
        if self.tajetasVolteadas < self.contMax:
            #self.mensajeEmergente("imagen 4")
            self.img4.setPixmap(QtGui.QPixmap(
                self.listaImagenesDisponibles[self.ordenImagenesMemorama[3]][1]
            ))
            self.tajetasVolteadas += 1

    def validar(self):
        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())