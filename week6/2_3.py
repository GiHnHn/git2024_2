import RPi.GPIO as GPIO
import time

BUZZER_PIN = 12
SW = [5,6,13,19]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.setup(SW, GPIO.IN,  pull_up_down=GPIO.PUD_DOWN)


p = GPIO.PWM(BUZZER_PIN, 440)
p.start(50)
p.ChangeDutyCycle(0)

melody = [(330, 0.5),(330, 0.5),(349, 0.5),(392, 0.5),(392, 0.5),(349, 0.5),(330, 0.5),(294, 0.5),
 (262, 0.5),(262, 0.5),(294, 0.5),(330, 0.5),(330, 0.5),(294, 1.0),
 (330, 0.5),(330, 0.5),(349, 0.5),(392, 0.5),(392, 0.5),(349, 0.5),(330, 0.5),(294, 0.5),
 (262, 0.5),(262, 0.5),(294, 0.5),(330, 0.5),(294, 1.0),(262, 0.2), (262, 2.0)]


def play_melody(melody):
    for freq, duration in melody:
        p.ChangeFrequency(freq)
        time.sleep(duration)


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(SW[0],GPIO.IN,pull_up_down=GPIO.PUD_DOWN)


def callback_func1(pin):
    if pin == SW[0]:
        p.ChangeDutyCycle(50)
        play_melody(melody)
        p.ChangeDutyCycle(0)
        

try:
    GPIO.add_event_detect(SW[0], GPIO.RISING, callback=callback_func1, bouncetime=300)

    while True:
        time.sleep(0.1)
        

except KeyboardInterrupt:
    pass

GPIO.cleanup()