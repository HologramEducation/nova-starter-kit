# 01 - Blink an LED

We'll be interacting with General Purpose Input/Output Pins (GPIO for short). For a quick refresher on the major nuances of Pi GPIO pins, check out this [StackOverflow]( https://raspberrypi.stackexchange.com/questions/12966/what-is-the-difference-between-board-and-bcm-for-gpio-pin-numbering). For this project we'll be using BCM numbering.

Posting the PINOUT here for quick reference:
<img src="https://s3.amazonaws.com/hologram-devrel-images/%5Bgithub%5Draspi-iot-workshop/01A00.png" width="690">

Also, for those not familiar with breadboards, [check out this video by ScienceBuddiesTv explaining how electricity runs through a breadboard](https://www.youtube.com/watch?v=6WReFkfrUIk).

In the first lesson we're setting a pin as an output, to control electricity going to an LED.

## Wiring Diagram

<img src="https://s3.amazonaws.com/hologram-devrel-images/%5Bgithub%5Draspi-iot-workshop/01A01.png" width="690">
Note: Make sure to remove power to the Pi before wiring.

## Installing Dependencies

Power on the Pi, connect through SSH over WiFi ,and run the following commands.

1. Update installed packages: `$ sudo apt-get update`
2. Install project dependencies: `$ sudo apt-get install git git-core build-essential python-dev python-openssl python-smbus python3-pip python-pip screen`
3. Install Hologram's Python SDK: `$ curl -L hologram.io/python-install | bash`
  - If you ever need to update our SDK run: `$ curl -L hologram.io/python-update | bash`
4. Verify Hologram's SDK is >= version 0.5.23: `$ hologram version`

## Running Code
1. `git clone https://github.com/benstr/pi-starter-kit.git`
2. `cd pi-starter-kit/01_blink`
3. `sudo python main.py`
4. After you verify the script and hardware works, open `main.py` and `myLED.py` to inspect what we're doing.
    - `cat main.py`
    - `cat myLED.py`
5. We've added a few additional functions in `myLED.py`. Modify `main.py` to use some of these extra functions.
