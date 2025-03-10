
# -> pip install pyserial
import serial as controlador

#genera el canal de comunicacion y la inicializa...
arduino = controlador.Serial("COM?", baudrate=9600, timeout=1)

while True:
    accion = input("Ingresa el valor de accion para el led: ") ##1 = prender....
    arduino.write(accion.encode())