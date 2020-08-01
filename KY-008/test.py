import RPi.GPIO as GPIO
import time

#GPIO Setup   
GPIO_14="cable verde"
GPIO_15="cable rojo"
VCC="cable amarillo"
GND="cable naranja"



GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.output(14, True)

def intermitent():
    while True:
        GPIO.output(14, True)
        time.sleep(1)
        GPIO.output(14, False)
        time.sleep(1)
    GPIO.cleanup()

if __name__=='__main__':
    intermitent()
    GPIO.cleanup()


