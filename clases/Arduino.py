import serial
import time

class ArduinoSerialCommunication:
    def __init__(self, port, baudrate=9600, timeout=1):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial_connection = None

    def connect(self):
        try:
            self.serial_connection = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                timeout=self.timeout
            )
            print(f"Conectado a {self.port} a {self.baudrate} baudios.")
        except serial.SerialException as e:
            print(f"Error al conectar: {e}")

    def disconnect(self):
        if self.serial_connection:
            self.serial_connection.close()
            print("Desconectado.")

    def send_data(self, data):
        if self.serial_connection and self.serial_connection.is_open:
            try:
                self.serial_connection.write(data.encode())
                print(f"Dato enviado: {data}")
            except serial.SerialException as e:
                print(f"Error al enviar dato: {e}")
        else:
            print("No hay conexión serial establecida.")

    def receive_data(self):
        if self.serial_connection and self.serial_connection.is_open:
            try:
                received_data = self.serial_connection.readline().decode().strip()
                print(f"Dato recibido: {received_data}")
                return received_data
            except serial.SerialException as e:
                print(f"Error al recibir dato: {e}")
        else:
            print("No hay conexión serial establecida.")