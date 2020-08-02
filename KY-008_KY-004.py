import RPi.GPIO as GPIO
import time

#GPIO Setup   
GPIO_14="cable verde"
GPIO_15="cable rojo"
VCC="cable amarillo"
GND="cable naranja"


GPIO_PIN_IN = 15
GPIO_PIN_OUT = 14

GPIO.setmode(GPIO.BCM)

GPIO.setup(GPIO_PIN_OUT, GPIO.OUT)
GPIO.setup(GPIO_PIN_IN, GPIO.IN)




def intermitent():
    while True:
        if GPIO.input(GPIO_PIN_IN):
            GPIO.output(GPIO_PIN_OUT, True)
        else:
            GPIO.output(GPIO_PIN_OUT, False)



if __name__=='__main__':
    intermitent()
    GPIO.cleanup()


