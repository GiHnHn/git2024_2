import RPi.GPIO as GPIO
import time

BUZZER_PIN = 12
SWITCH_PIN = 5

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # 풀업 저항 사용

p = GPIO.PWM(BUZZER_PIN, 440)
p.start(0)  # 초기 duty cycle을 0으로 설정하여 소리 없음

# 멜로디와 박자 설정
melody = [
    (330, 0.5), (330, 0.5), (349, 0.5), (392, 0.5), (392, 0.5), (349, 0.5), (330, 0.5), (294, 0.5),
    (262, 0.5), (262, 0.5), (294, 0.5), (330, 0.5), (330, 0.5), (294, 1.0),
    (330, 0.5), (330, 0.5), (349, 0.5), (392, 0.5), (392, 0.5), (349, 0.5), (330, 0.5), (294, 0.5),
    (262, 0.5), (262, 0.5), (294, 0.5), (330, 0.5), (294, 1.0), (262, 0.2), (262, 2.0)
]

# 멜로디 재생 함수
def play_melody(melody):
    for freq, duration in melody:
        p.ChangeFrequency(freq)
        p.ChangeDutyCycle(50)  # 부저 소리를 위해 duty cycle 설정
        time.sleep(duration)
    p.ChangeDutyCycle(0)  # 멜로디 재생이 끝나면 소리를 끔

# 버튼이 눌릴 때 호출할 콜백 함수
def play_melody_callback(channel):
    play_melody(melody)

# 이벤트 감지 설정
GPIO.add_event_detect(SWITCH_PIN, GPIO.FALLING, callback=play_melody_callback, bouncetime=300)

try:
    while True:
        time.sleep(1)  # 대기 상태 유지
except KeyboardInterrupt:
    pass
finally:
    p.stop()
    GPIO.cleanup()
