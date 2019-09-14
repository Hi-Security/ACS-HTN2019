import serial
import time
import binascii


def packIntegerAsULong(value):
    """Packs a python 4 byte unsigned integer to an arduino unsigned long"""
    return struct.pack('I', value)    #should check bounds

# To see what it looks like on python side
val = 15000
print(binascii.hexlify(port.packIntegerAsULong(val)))

# send and receive via pyserial
ser = serial.Serial(serialport, bps, timeout=1)
ser.write(packIntegerAsULong(val))
line = ser.readLine()
print(line)