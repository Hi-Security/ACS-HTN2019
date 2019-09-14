import serial

import time

y_cons = 1.8
x_cons = 1.8

# 1 for x
# 2 for y
# 1 for pos
# 0 for neg
def send(x,y):
    message = [None] * 8
    if (x >= 0): #positive
        message[0] = 1
        message[1] = 1
        #convert to char
        #send positive char
    elif(x<0):
        message[0] = 1
        message[1] = 0

    x = abs(int(x/10)) #reduce power by 10 times
    if (abs(x)>70):
        x = 70
    ten =int(x/10)
    single = int(x%10)
    message[2] = ten
    message[3] = single


    if (y >=0): #positive
        message[4] = 2
        message[5] = 1
    elif(y<0):
        message[4] = 2
        message[5] = 0
    y = abs(int(y/10))
    if (abs(y)>70):
        y = 70
    ten =int(y/10)
    single = int(y%10)
    message[6] = ten
    message[7] = single
    for i in range(8):
        #print(message[i])
        ser.write(message[i])

def PID (x_pix, y_pix):
    x_power = x_pix * x_cons
    y_power = y_pix * y_cons
    send(x_power, y_power)

if __name__ == "__main__":
    arduinoport = 'com3'
    ser = serial.Serial(arduinoport, 9600)
    send(510,-320)
