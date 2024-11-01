import serial
import threading
import time
import RPi.GPIO as GPIO



GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
PWMA = 18
PWMB = 23
AIN1 = 22
AIN2 = 27
BIN1 = 25
BIN2 = 24
Btn = [22, 27, 25, 24]

GPIO.setup(PWMA, GPIO.OUT)
GPIO.setup(PWMB, GPIO.OUT)
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)
GPIO.setup(BIN1, GPIO.OUT)
GPIO.setup(BIN2, GPIO.OUT)

L_Motor = GPIO.PWM(PWMA, 500)
R_Motor = GPIO.PWM(PWMB, 500)
L_Motor.start(0)
R_Motor.start(0)
 

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
                GPIO.output(AIN1, 0)
                GPIO.output(AIN2, 1)
                GPIO.output(BIN1, 0)
                GPIO.output(BIN2, 1)
                L_Motor.ChangeDutyCycle(50)
                R_Motor.ChangeDutyCycle(50)
            elif gData.find("B0") >= 0:
                gData = ""
                print("ok back")
                GPIO.output(AIN1, 1)
                GPIO.output(AIN2, 0)
                GPIO.output(BIN1, 1)
                GPIO.output(BIN2, 0)
                L_Motor.ChangeDutyCycle(50)
                R_Motor.ChangeDutyCycle(50)
            elif gData.find("B2") >= 0:
                gData = ""
                print("ok left")
                GPIO.output(AIN1, 1)
                GPIO.output(AIN2, 0)
                GPIO.output(BIN1, 0)
                GPIO.output(BIN2, 1)
            elif gData.find("B3") >= 0:
                gData = ""
                print("ok right")
                GPIO.output(AIN1, 0)
                GPIO.output(AIN2, 1)
                GPIO.output(BIN1, 1)
                GPIO.output(BIN2, 0)
                L_Motor.ChangeDutyCycle(50)
                R_Motor.ChangeDutyCycle(50)
            elif gData.find("B1") >= 0:
                gData = ""
                print("ok stop")
                GPIO.output(AIN1, 0)
                GPIO.output(AIN2, 0)
                GPIO.output(BIN1, 0)
                GPIO.output(BIN2, 0)
                L_Motor.ChangeDutyCycle(50)
                R_Motor.ChangeDutyCycle(50)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    task1 = threading.Thread(target=serial_thread)
    task1.start()
    main()
    bleSerial.close()
    GPIO.cleanup() 

