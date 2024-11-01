import serial
import threading
import time

bleSerial = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1.0)

gData = ""

try:
    while True:
        data = bleSerial.readline()
        data = data.decode()
        print(data)

except KeyboardInterrupt:
    pass

bleSerial.close()