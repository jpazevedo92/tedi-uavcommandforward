import time
import serial
import threading

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
	port='COM8',
	baudrate=9600,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS
)

ser.close()
ser.open()
ser.isOpen()

while 1:
	print("Waiting for data\r")
	data = ser.readline().decode()
	print(data)



