import serial
import time
import binascii
from struct import *

def packIntegerAsULong(value):
    """Packs a python 4 byte unsigned integer to an arduino unsigned long"""
    return pack('I', value)    #should check bounds

val = 15000
print (binascii.hexlify(packIntegerAsULong(val)))

try:
    arduinoData = serial.Serial('COM4',9600)
    time.sleep(1)
    print("Connection to COM3 established succesfully!\n")
except Exception as e:
    print(e)

arduinoData.write(packIntegerAsULong(val))
print("reading data")
line = arduinoData.readline()
print (line)
print("complete")
