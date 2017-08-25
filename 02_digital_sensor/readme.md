# 02 - Read a Digital Sensor

In this step we'll read from a digital sensor, the DHT11. This sensor reads humidity and temperature, sending the results through a digital signal. The Pi's pins can read digital sensors out of the box.

The new code in this lesson adds `myDHT.py`. In this file we set a pin as an input and create some common functions. Adafruit's DHT python library is the real star, making it super simple to read the DHT chip.

You can read ore about DHT sensors on Adafruit: https://learn.adafruit.com/dht

## Wiring Diagram

<img src="https://s3.amazonaws.com/hologram-devrel-images/%5Bgithub%5Draspi-iot-workshop/02A00.png" width="690">
Note: Make sure to remove power to the Pi before wiring.

## Running Code

Power on the Pi, connect through SSH over WiFi ,and run the following commands.

1. Install the DHT python library
    - ```
      cd ~
      git clone https://github.com/adafruit/Adafruit_Python_DHT.git
      cd Adafruit_Python_DHT
      ```
    - Install library `sudo python setup.py install`
    - Test library `sudo ./examples/AdafruitDHT.py 11 21`
        - We're passing `11` since the sensor is a DHT11, `21` is the pin the sensor is wired to.
2. `cd pi-starter-kit/02_digital_sensor`
3. Run `sudo python main.py`, the LED should blink 3 times and the rooms temp + humidity should print to the terminal.
4. After you verify the script and hardware works, open `main.py` and `myDHT.py` to inspect what we're doing.
    - `cat main.py`
    - `cat myDHT.py`
5. We've added a few additional functions in `myDHT.py`. Modify `main.py` to use some of these extra functions.
