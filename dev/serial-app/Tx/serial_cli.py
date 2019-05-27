####
##   Command Line Interface for TEDI 2018/19
##   1111476 - Joao Pedro Azevedo
####

#!/usr/bin/env python
import time
import serial

choices = {'c':'c', 'a':'a'}
send_array = []
send_string = ""

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
	port='/dev/ttyUSB0',
	baudrate=115200,
	bytesize=serial.EIGHTBITS,
	parity=serial.PARITY_NONE,
	stopbits = serial.STOPBITS_ONE


)

ser.close()
ser.open()
#ser.close()
ser.isOpen()


def menu_entry(option):
	global send_string
	if option == 'c':
		n_uavs = int(input("Drones of network: "))
		for x in range(0, n_uavs):
			command = input("Introduce a command for drone " + str(x+1) + ": ")
			uav_no = x+1
			send_string += str(uav_no) + "_" + command + "_"
			#uav_array = [ uav_no, command ]
			#send_array.append(uav_array)

		#str_to_send = str(n_uavs)+"|"+str(send_array)+"\r\n"
		str_to_send = str(n_uavs)+"|"+send_string+"\r\n"
		ser.write(str_to_send.encode())
		print(str_to_send)
		time.sleep(1)
	elif option == 'a':
		print("A")
	else:
		print('Bye Bye!')

def menu_show():
	print("Press 'c' to create a network")
	print("Press 'a' to add a new element to a network")
	option_input = input("Choose one option: ")
	option = choices.get(option_input, 'Quit Program! ')
	menu_entry(option)

while 1 :
	menu_show()
	old_string = send_string
	send_string = ""
	#old_array = send_array
	#send_array = []



