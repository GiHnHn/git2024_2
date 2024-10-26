import RPi.GPIO as GPIO
import time

BUZZER_PIN = 12

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

p = GPIO.PWM(BUZZER_PIN, 440)
p.start(50) 

melody = [262, 294, 330, 349, 392, 440, 494, 523]


def play_melody(melody, duration=0.5):
    for freq in melody:
        p.ChangeFrequency(freq)
        time.sleep(duration)

try:
    while True:   
        play_melody(melody)  
        time.sleep(1.0)  
except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()
