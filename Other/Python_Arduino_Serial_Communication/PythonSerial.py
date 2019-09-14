import serial
import time

arduinoport = 'COM3'
arduino_data = serial.Serial(arduinoport,9600)

#arduino_data.write(b'1')
Constant_X = 0.1
Constant_Y = 0.1

i = 0
while (true):
    while i < 50:
        arduino_data.write([i])



#def pid_control(pix_x, pix_y):





def serialwrite(x,y):
    if x>0: #x is positive
        x = 2000+x
    else:
        x = 1000+x

    if y>0: #y is positive
        y = 2000+y
    else:
        y = 1000+y

    x= 1000*x
    encoded_coor = x+y
    arduino_data.write([encoded_coor])

