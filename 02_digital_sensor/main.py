import RPi.GPIO as GPIO ## Import GPIO library
from myLED import blink ## Import blink function
from myDHT import getTempString, getHumString ## Import temperature and humidity functions

GPIO.setmode(GPIO.BCM) ## Use broadcom pin numbering

LED_PIN = 17 ## GPIO pin the LED is attached to
DHT_PIN = 21 ## GPIO pin the DHT sensor is attached to

## Exercise 01 - blink an LED
## blinkTimes(LED_PIN) ## blink the LED

## Exercise 02 - read a digital sensor
blink(LED_PIN) ## blink the LED
print getTempString(DHT_PIN) ## print temp string to terminal
blink(LED_PIN)
print getHumString(DHT_PIN) ## print hum string to terminal
blink(LED_PIN)

GPIO.cleanup()  ## reset all pins
