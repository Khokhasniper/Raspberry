
from gpiozero import Servo
from gpiozero import Button
from time import sleep  
button = Button(18)
servo=Servo(17)

def ButtonedServo():
    if button.is_pressed:
     
        servo.max()
        sleep(0.5)
        servo.mid()
        sleep(0.5)
        servo.max()
        sleep(0.5)
        servo.mid()
        sleep(0.5)
        servo.min()
while True:
    ButtonedServo()