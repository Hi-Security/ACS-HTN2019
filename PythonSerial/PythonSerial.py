import serial

import time

y_cons = 1.8
x_cons = 1.8

def send(x,y):
    message = [None] * 6
    if (x >= 0): #positive
        message[0] = 'x'
        message[1] = 'p'
        #convert to char
        #send positive char
    elif(x<0):
        message[0] = 'x'
        message[1] = 'n'

    x = abs(int(x/10)) #reduce power by 10 times
    if (abs(x)>70):
        x = 70
    message[2] = chr(x)


    if (y >=0): #positive
        message[3] = 'y'
        message[4] = 'p'
    elif(y<0):
        message[3] = 'y'
        message[4] = 'n'
    y = abs(int(y/10))
    if (abs(y)>70):
        y = 70
    message[5] = chr(y)

    for i in range(6):
        print(message[i])
        #ser.write(message[i])

def PID (x_pix, y_pix):
    x_power = x_pix * x_cons
    y_power = y_pix * y_cons
    send(x_power, y_power)

if __name__ == "__main__":
    arduinoport = 'com3'
    ser = serial.Serial(arduinoport, 9600)
    send(510,-320)
