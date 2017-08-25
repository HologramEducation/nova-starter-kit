import Adafruit_DHT ## Import temp/hum library

DHT_SENSOR = Adafruit_DHT.DHT11

def getHum(DHT_PIN):
    humidity = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)[0]

    if humidity is not None:
        return humidity
    else:
        return 'FAILED '

def getHumString(DHT_PIN):
    return 'Humidity = ' + str(humidity) + '%'

def getTemp(DHT_PIN):
    temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)[1]
    temperature = temperature * 9/5.0 + 32 ## Convert temp to Fahrenheit

    if temperature is not None:
        return temperature
    else:
        return 'FAILED '

def getTempString(DHT_PIN):
    return 'Temperature = ' + str(getTemp(DHT_PIN)) + 'F'
