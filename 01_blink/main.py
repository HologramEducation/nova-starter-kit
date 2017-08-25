import RPi.GPIO as GPIO ## Import GPIO library
from myLED import blinkTimes ## Import blink function

GPIO.setmode(GPIO.BCM) ## Use broadcom pin numbering

LED_PIN = 17 ## GPIO pin the LED is attached to

## Exercise 01 - blink an LED
blinkTimes(LED_PIN) ## blink the LED

GPIO.cleanup()  ## reset all pins
