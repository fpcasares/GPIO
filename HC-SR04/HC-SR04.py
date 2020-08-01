import RPi.GPIO as GPIO
import time

#GPIO Setup   
GPIO_14="cable verde"
GPIO_15="cable rojo"
GPIO_18="cable blanco"
VCC="cable amarillo"
GND="cable naranja"
3V='cable azul"

TRIGGER = 15
ECHO = 18
GPIO_PIN_OUT = 14

GPIO.setmode(GPIO.BCM)

GPIO.setup(GPIO_PIN_OUT, GPIO.OUT)
GPIO.setup(TRIGGER,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)



GPIO.output(TRIG,False)
print('Waiting for Sensor to Settle")
time.sleep(2)

GPIO.output(TRIG,True)
time.sleep(0.00001)
GPIO.output(TRIG,False)

while GPIO.input(ECHO)==0:
  pulse_start = time.time()

while GPIO.input(ECHO)==1:
  pulse_end = time.time()   


pulse_duration =pulse_end - pulse_start  

distance= pulse_duration * 17150
distance = rount(distance,2)

print ("Distance: ",distance," cm")

GPIO.cleanup()
