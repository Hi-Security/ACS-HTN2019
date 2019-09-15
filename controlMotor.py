#!/usr/bin/python
import serial
import time
import string
X_CONST = 4
Y_CONST = 4
TOLERANCE = 50

port = 'COM3' # note I'm using Mac OS-X
#NOTE: THIS MAY DIFFER FOR COMPUTER
ard = serial.Serial(port,9600,timeout=5)
time.sleep(2) # wait for Arduino


def pid(x,y):
    global port, X_CONST, Y_CONST, TOLERANCE
    x_power= -1*x*X_CONST
    y_power = -1*y*Y_CONST
    message = ""
    if x_power >= 0:
        message+="P"


    else:
        message +="N"

    if abs(x_power) > 720:
        x_power = 720
    x_power_string = str(abs(x_power))
    while len(x_power_string)<3:
        x_power_string= '0'+x_power_string
    message+=x_power_string

    if y_power >= 0:
        message+="P"


    else:
        message+="N"

    if abs(y_power) > 720:
        y_power= 720

    y_power_string = str(abs(y_power))
    while len(y_power_string)<3:
        y_power_string= '0'+y_power_string
    message+=y_power_string

    print("y " + str(y_power))
    print("x " + str(x_power))
    print(message)
    #print("Python Message " + message)
    ard.flush()
    ard.write(str(message).encode())



if __name__== "__main__":
    while (True):
    # Serial write section
        ard = serial.Serial(port, 9600, timeout=5)
        time.sleep(2)  # wait for Arduino

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