import RPi.GPIO as GPIO
import time

BUZZER = 12
SW = [5, 6, 13, 19]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(SW[0], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW[1], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW[2], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW[3], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BUZZER, GPIO.OUT)

p = GPIO.PWM(BUZZER, 261)
p.start(0)


Freq = [262, 294, 330, 349]
button_states = [False, False, False, False]

try:
    while True:
        for i in range(4):
            if GPIO.input(SW[i]) == GPIO.HIGH:
                if not button_states[i]:
                    p.ChangeFrequency(Freq[i])
                    p.ChangeDutyCycle(50)
                    button_states[i] = True
            else:
                if button_states[i]:  
                    p.ChangeDutyCycle(0)
                    button_states[i] = False

        time.sleep(0.05)  

except KeyboardInterrupt:
    pass

p.stop()        
GPIO.cleanup()  