import RPi.GPIO as GPIO
import time

SW = [5,6,13,19]


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(SW[0],GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW[1],GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW[2],GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW[3],GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

SwC = [0, 0, 0, 0]
SwList = []

def callback_func1(pin):
    if pin == SW[0]:
        SwC[0] += 1
        print(f"('SW1 click', {SwC[0]})")
        SwList.append("SW1")
        print(SwList, "\n")

    elif pin == SW[1]:
        SwC[1] += 1
        print(f"('SW2 click', {SwC[1]})")
        SwList.append("SW2")
        print(SwList, "\n")

    elif pin == SW[2]:
        SwC[2] += 1
        print(f"('SW3 click', {SwC[2]})")
        SwList.append("SW3")
        print(SwList, "\n")

    elif pin == SW[3]:
        SwC[3] += 1
        print(f"('SW4 click', {SwC[3]})")
        SwList.append("SW4")
        print(SwList, "\n")


try:
    GPIO.add_event_detect(SW[0], GPIO.RISING, callback=callback_func1, bouncetime=300)
    GPIO.add_event_detect(SW[1], GPIO.RISING, callback=callback_func1, bouncetime=300)
    GPIO.add_event_detect(SW[2], GPIO.RISING, callback=callback_func1, bouncetime=300)
    GPIO.add_event_detect(SW[3], GPIO.RISING, callback=callback_func1, bouncetime=300)

    while True:
        time.sleep(0.1)
        

except KeyboardInterrupt:
    pass

GPIO.cleanup()