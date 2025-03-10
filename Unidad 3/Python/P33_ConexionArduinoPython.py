
# -> pip install pyserial
import serial as controlador

#genera el canal de comunicacion y la inicializa...
arduino = controlador.Serial("COM?", baudrate=9600, timeout=1)

