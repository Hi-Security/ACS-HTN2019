#!/usr/bin/python
import serial
import time
import string
X_CONST = 4
Y_CONST = 4
TOLERANCE = 50


def pid(x,y):
    x_power= x*X_CONST
    y_power = y*Y_CONST
    message = ""
    if x_power >= 0:
        message+="P"


    else:
        message +="N"

    if abs(x_power) > 720:
        x_power = 720
    x_power_string = str(abs(x_power))
    message+=x_power_string

    if y_power >= 0:
        message+="P"


    else:
        message+="N"

    if abs(y_power) > 720:
        y_power= 720

    y_power_string = str(abs(y_power))
    message+=y_power_string
    #print("Python Message " + message)
    return message



#The following line is for serial over GPIO
port = 'COM3' # note I'm using Mac OS-X


ard = serial.Serial(port,9600,timeout=5)
time.sleep(2) # wait for Arduino



while (True):
    # Serial write section

    setTempCar1 = pid(400,-400) #hey steven, update this variable to send
    ard.flush()
    setTemp1 = str(setTempCar1)

    #print ("Python value sent: ")
    #print (setTemp1)
    ard.write(setTemp1.encode())
    time.sleep(0.002) # I shortened this to match the new value in your Arduino code

    #Serial Read session
   # msg = ard.read(ard.inWaiting()) # read all characters in buffer
    #print ("Message from arduino: ")
    #print (msg.decode())


else:
   print ("Exiting")
#exit()