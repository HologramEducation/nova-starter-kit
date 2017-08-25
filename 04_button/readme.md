# 04 - Trigger with a Button

Ok, we have a fully functioning set of sensors! But, triggering the script through a terminal in a SSH session is not ideal. In this lesson we setup a button to trigger a reading and set the script to continuously loop after the pi boots.

## Wiring Diagram

<img src="https://s3.amazonaws.com/hologram-devrel-images/%5Bgithub%5Draspi-iot-workshop/04A00.png" width="690">
Note: Make sure to remove power to the Pi before wiring.

## Running Code

Power on the Pi, connect through SSH over WiFi ,and run the following commands.

1. `cd ../04_button`
3. Run `sudo python main.py`, nothing should happen.
4. Press the button, the LED should blink 4 times and sensor values should print in the terminal. Cover up the light sensor or breath on the DHT sensor then press the button to see the changed values.
5. Exit the loop by CTRL + C
6. After you verify the script and hardware works, open `main.py` to inspect what we're doing.
    - `cat main.py`

## Running at Startup

We have a button and sensors, yay! but we still need the terminal to start the python script. Lets set the Pi to automatically run this script at startup.

1. Run `sudo nano /etc/rc.local`
2. Add `sudo python /home/pi/pi-starter-kit/04_button/main.py.py &` BEFORE `exit0`
3. Save and exit the file. Reboot the pi by running `sudo reboot`.
4. After a few minutes, press the button and if the light flashes 4 times then it worked!
5. Now every time you power the Pi this script will be running in the background.
