import serial
import time

arduino = serial.Serial('COM12', 9600)

time.sleep(2)
arduino.write(b'0')  # Puedes cambiar esto a '2' si es necesario
arduino.close()