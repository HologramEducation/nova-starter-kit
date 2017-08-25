# 03 - Read an Analog Sensor

In the last lesson we read from a digital sensor, the sensor sent digital values. There is another way sensors can communicate called analog. Analog sensors send the raw value of electrons traveling through them. Depending on the type of sensor determines what these random numbers mean.

All Raspberry Pi's can only read digital sensors. In order to read analog sensors we'll need to an Analog-2-Digital Converter (ADC or ADS) between the analog sensor and the Pi. The ADC will convert the analog signal into a digital output and send it to the Pi.

In this lesson we're setting up an MCP-3008 converter to read a light sensor (officially called a photoresistor). We're adding our light sensor functions in `myMCP.py` and adding another Adafruit python library, this time for the MCP chip.

One more note on the MCP-3008. It provides 8 ports, meaning it can read up to 8 analog sensors. We're using port 0. In main.py you'll notice we set which port the photoresistor is using as a global.

    - [Read more about the MCP-3008](https://learn.adafruit.com/raspberry-pi-analog-to-digital-converters/mcp3008)
    - [Read more about photoresistors](https://en.wikipedia.org/wiki/Photoresistor)

## Wiring Diagram

<img src="https://s3.amazonaws.com/hologram-devrel-images/%5Bgithub%5Draspi-iot-workshop/03A00.png" width="690">
Note: Make sure to remove power to the Pi before wiring.

## Running Code

Power on the Pi, connect through SSH over WiFi ,and run the following commands.

1. Install the MCP python library
    - ```
      cd ~
      git clone https://github.com/adafruit/Adafruit_Python_MCP3008.git
      cd Adafruit_Python_MCP3008
      ```
    - Install library `sudo python setup.py install`
2. `cd pi-starter-kit/03_analog_sensor`
3. Run `sudo python main.py`, the LED should blink 4 times and the rooms temp + humidity + brightness should print to the terminal.
4. After you verify the script and hardware works, open `main.py` and `myMCP.py` to inspect what we're doing.
    - `cat main.py`
    - `cat myMCP.py`
5. We've added a few additional functions in `myMCP.py`. Modify `main.py` to use some of these extra functions.
