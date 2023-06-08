import RPi.GPIO as GPIO
from time import sleep
#led = LED(18)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pir_gpio = 17
GPIO.setup(pir_gpio, GPIO.IN)
while True:
    if GPIO.input(pir_gpio) == 1:
        #led.on()
        GPIO.output(18,GPIO.HIGH)
        print('there is motion')
        sleep(1)
    elif GPIO.input(pir_gpio) == 0:
        #led.off()
        GPIO.output(18,GPIO.LOW)
        print('There isnt motion')
        sleep(1)
