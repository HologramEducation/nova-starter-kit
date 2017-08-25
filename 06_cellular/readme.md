# 06 - Sending Data through Cellular

We are rocking! Now lets get cellular rolling. It's very similar steps from the last lesson.

## Running Code

Power on the Pi, connect through SSH over WiFi ,and run the following commands.

1. Plug in your USB modem
1. Run `sudo nano /etc/rc.local`
2. Change our script path to `sudo python /home/pi/pi-starter-kit/06_cellular/main.py.py &` BEFORE `exit0`
3. Save and exit the file. Reboot the pi by running `sudo reboot`.
4. After a few minutes, press the button and if the light flashes 4 times then it worked!
5. On a separate computer go to [https://dashboard.hologram.io/?drawer=full](https://dashboard.hologram.io/?drawer=full) to see the data from the device!
6. After you verify the script and hardware works, open `main.py` to inspect what we're doing.
    - `cat pi-starter-kit/06_cellular/main.py`
