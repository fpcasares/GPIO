# needed modules will be imported
import RPi.GPIO as GPIO
import time
  
GPIO.setmode(GPIO.BCM)
  
# The input pin of the Sensor will be declared. Additional to that the pull-up resistor will be activated.
GPIO_PIN_OUT=14
GPIO_PIN_IN = 15
GPIO.setup(GPIO_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(GPIO_PIN_OUT, GPIO.OUT)


on_status=False


def ON():
    print("Signal detected")
    if not on_status:
        GPIO.output(GPIO_PIN_OUT, True)
        on_status=True
    if on_status:
        GPIO.output(GPIO_PIN_OUT, False)
        on_status=False
    
    
  
print "Sensor-Test [press ctrl+c to end it]"
  
# This output function will be started at signal detection.

        
  
# At the moment of detecting a Signal ( falling signal edge ) the output function will be activated.
GPIO.add_event_detect(GPIO_PIN_IN, GPIO.FALLING, callback=ON, bouncetime=100) 
  
# main program loop
try:
        while True:
                time.sleep(1)
  
# Scavenging work after the end of the program
except KeyboardInterrupt:
        GPIO.cleanup()