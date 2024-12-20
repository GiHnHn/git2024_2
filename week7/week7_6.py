import serial
import threading
import time

bleSerial = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1.0)

gData = ""

def serial_thread():
    global gData
    while True:
        data = bleSerial.readline()
        data = data.decode()
        gData = data

def main():
    global gData
    try:
        while True:
            if gData.find("B5") >= 0:
                gData = ""
                print("ok go")
            elif gData.find("B0") >= 0:
                gData = ""
                print("ok back")
            elif gData.find("B2") >= 0:
                gData = ""
                print("ok left")
            elif gData.find("B3") >= 0:
                gData = ""
                print("ok right")
            elif gData.find("B1") >= 0:
                gData = ""
                print("ok stop")
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    task1 = threading.Thread(target=serial_thread)
    task1.start()
    main()
    bleSerial.close()

