import RPi.GPIO as GPIO
import time


SW = [5, 6, 13, 19]

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
GPIO.setup(SW[0], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW[1], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW[2], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW[3], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

L_Motor = GPIO.PWM(PWMA, 500)
R_Motor = GPIO.PWM(PWMB, 500)
L_Motor.start(0)
R_Motor.start(0)

button_states = [False, False, False, False]

def control(pin):
    if pin == SW[0]:
        GPIO.output(AIN1, 0)
        GPIO.output(AIN2, 1)
        GPIO.output(BIN1, 0)
        GPIO.output(BIN2, 1)
        L_Motor.ChangeDutyCycle(50)
        R_Motor.ChangeDutyCycle(50)
        print("SW1")
    elif pin == SW[1]:
        GPIO.output(AIN1, 0)
        GPIO.output(AIN2, 1)
        GPIO.output(BIN1, 1)
        GPIO.output(BIN2, 0)
        L_Motor.ChangeDutyCycle(50)
        R_Motor.ChangeDutyCycle(50)
        print("SW2")
    elif pin == SW[2]:
        GPIO.output(AIN1, 1)
        GPIO.output(AIN2, 0)
        GPIO.output(BIN1, 0)
        GPIO.output(BIN2, 1)
        L_Motor.ChangeDutyCycle(50)
        R_Motor.ChangeDutyCycle(50)
        print("SW3")
    elif pin == SW[3]:
        GPIO.output(AIN1, 1)
        GPIO.output(AIN2, 0)
        GPIO.output(BIN1, 1)
        GPIO.output(BIN2, 0)
        L_Motor.ChangeDutyCycle(50)
        R_Motor.ChangeDutyCycle(50)
        print("SW4")


try:
    while True:
        for i in range(4):
            if GPIO.input(SW[i]) == GPIO.HIGH:
                if not button_states[i]:
                    control(SW[i])
                    button_states[i] = True
            else:
                if button_states[i]:  
                    L_Motor.ChangeDutyCycle(0)
                    R_Motor.ChangeDutyCycle(0)
                    button_states[i] = False

        time.sleep(0.05)  

except KeyboardInterrupt:
    pass
    
GPIO.cleanup()  



