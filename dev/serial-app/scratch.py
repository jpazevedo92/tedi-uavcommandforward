
def read_from_port(ser):
    while not connected:
    	print("Waiting for data\r")
        #serin = ser.read()
    connected = True
    while True:
       print("test")
       data = ser.readline().decode()
       #"utf-8"
       print(data)
       connected = False



while 1:
	# get keyboard input
	input_phrase = input("Type 'e' to exit program\r\n>> ")
	thread = threading.Thread(target=read_from_port, args=(ser))
	thread.start()
	if input_phrase=='e':
		ser.close()
		exit()	