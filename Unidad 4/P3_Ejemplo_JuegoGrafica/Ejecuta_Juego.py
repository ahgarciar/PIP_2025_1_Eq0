import sys

from PyQt5 import QtWidgets

import Plantilla_Juego as grafica
import matplotlib.pyplot as plt

class MyApp(QtWidgets.QMainWindow, grafica.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        grafica.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals / Configuracion
        self.btn_action.clicked.connect(self.action)

        self.btn_arriba.clicked.connect(self.mover)
        self.btn_izquierda.clicked.connect(self.mover)
        self.btn_centro.clicked.connect(self.mover)
        self.btn_derecha.clicked.connect(self.mover)
        self.btn_abajo.clicked.connect(self.mover)

        ################################################################################

        self.xMax = 5
        self.xMin = -5
        self.yMax = 5
        self.yMin = -5

        #################################################################################
        #
        self.enemigos = []  # enemigos
        self.jugador = [0, 0]  # jugador 1
        self.enemigos_vivos = 0
        ##############################################

        self.limpiar()


    # Área de los Slots
    def action(self):
        if self.btn_action.text() == "INICIAR":
            self.btn_action.setText("DETENER")

            #jugador
            self.jugador = [0, 0] #vuelve al jugar al centro

            import random as rnd
            #posiciona a los enemigos en posiciones aleatorias

            total_enemigos = 6
            self.enemigos_vivos = total_enemigos
            self.enemigos = []
            while total_enemigos > 0:
                new_enemigo = [rnd.randrange(self.xMin, self.xMax),
                                      rnd.randrange(self.yMin, self.yMax)]
                #comprueba que las coordenadas del enemigo no esten superpuestas con otro enemigo
                duplicated = False
                if new_enemigo[0] == self.jugador[0] and new_enemigo[1] == self.jugador[1]:
                    duplicated = True
                else:
                    for enemigo in self.enemigos:
                        if enemigo[0] == new_enemigo[0] and enemigo[1] == new_enemigo[1]:
                            duplicated = True
                            break

                if not duplicated:
                    self.enemigos.append(new_enemigo)
                    total_enemigos -= 1

            self.graficar()
        else:
            self.btn_action.setText("INICIAR")
            self.limpiar()

    def mover(self):
        nombre_boton = self.sender().objectName()
        accion = nombre_boton.split("_")[1]  # [0] = btn -- [1] = abajo
        print(nombre_boton, " accion:", accion)
        #UBICACION ACTUAL EN EL PLANO DEL USUARIO...
        Xusuario = self.jugador[0]  # [0] = valor de X del usuario
        Yusuario = self.jugador[1]  # [1] = valor de Y del usuario
        if accion == "arriba":  # v  => valor de y
            if Yusuario + 1 <= self.yMax:
                self.jugador[1] = Yusuario + 1
            else:
                self.jugador[1] = self.yMin
        elif accion == "abajo":  # v  => valor de y
            if Yusuario - 1 >= self.yMin:
                self.jugador[1] = Yusuario - 1
            else:
                self.jugador[1] = self.yMax
        elif accion == "izquierda":  # v  => valor de x
            if Xusuario - 1 >= self.xMin:
                self.jugador[0] = Xusuario - 1
            else:
                self.jugador[0] = self.xMax
        elif accion == "derecha":  # v  => valor de x
            if Xusuario + 1 <= self.xMax:
                self.jugador[0] = Xusuario + 1
            else:
                self.jugador[0] = self.xMin
        else: #centro
            self.jugador[0] = 0
            self.jugador[1] = 0
        self.limpiar()
        self.graficar()

    def limpiar(self):
        plt.cla() #BORRA_TODO EL GRAFICO

        x = [i for i in range(self.xMin, self.xMax + 1)] #GENERA LOS TICKS
        y = [i for i in range(self.yMin, self.yMax + 1)] #GENERA LOS TICKS

        self.ax.set_xticks(x)
        self.ax.set_yticks(y)

        # Establecer los limites
        self.ax.set_xlim(self.xMin, self.xMax)
        self.ax.set_ylim(self.yMin, self.yMax)

        plt.grid(True)  #CUADRICULA

        self.canvas.draw() #DIBUJAR EL GRAFICO


    def graficar(self):

        #POSICIONA AL USUARIO EN LA GRAFICA
        self.ax.plot(self.jugador[0], self.jugador[1],
                     marker="o",  # o . *  x   1
                     markersize=8,
                     markerfacecolor="yellow",  # color interno del marcador
                     markeredgewidth=1,  # tamaño del borde del marcador
                     markeredgecolor="black",  # color del borde del marcador
                     )

        #POSICIONA A LOS ENEMIGOS EN EL GRAFICO
        for enemigo in self.enemigos:
            self.ax.plot(enemigo[0], enemigo[1],
                         marker="o",  # o . *  x   1
                         markersize=8,
                         markerfacecolor="green",  # color interno del marcador
                         markeredgewidth=1,  # tamaño del borde del marcador
                         markeredgecolor="black",  # color del borde del marcador
                         )

        self.canvas.draw() #DIBUJA EL GRAFICO

        #COMPRUEBA CADA QUE SE GRAFICA SI EL USUARIO ALCANZO A ALGUN ENEMIGO
        #SI LAS COORDENADAS DE AMBOS ESTAN EN LA MISMA POSICION, ENTONCES EL USUARIO ALCANZO
        # AL ENEMIGO..
        for enemigo in self.enemigos:
            if self.jugador[0] == enemigo[0] and self.jugador[1] == enemigo[1]:
                self.enemigos_vivos-=1
                #PEND: eliminar al enemigo de la lista
                self.limpiar()
                self.graficar()
                m = QtWidgets.QMessageBox()
                m.setText("Has Eliminado a un enemigo!")
                m.exec_()

        if self.enemigos_vivos == 0:
            self.limpiar()
            m = QtWidgets.QMessageBox()
            m.setText("Has Ganado!")
            m.exec_()
            self.btn_action.setText("INICIAR")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

##TAREA:
#1.- Agregar el contador de tiempo
#2.- Agregar un contador visual de enemigos restantes o enemigos destruidos
#3.- Hacer que desaparezca visualmente un enemigo que ya elimine
#4.- Agregar diseño al programa (incluidas imagenes-logos)

