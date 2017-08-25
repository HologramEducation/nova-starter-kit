# 05 - Sending Data through WiFi

Our sensors script is running at startup, great! But we still need to SSH into the terminal to see the data. Instead lets send the data through WiFi to Hologram's Data Router (CSR).

If you haven't activated your Hologram SIM, please do so now: [https://dashboard.hologram.io/activate](https://dashboard.hologram.io/activate).

## Running Code

Power on the Pi, connect through SSH over WiFi ,and run the following commands.

1. Go to your device detail page through the [Hologram Dashboard](https://dashboard.hologram.io/).
2. Under the Configuration tab select Sow Router Credentials and save the 8 character key.
3. Back in the Pi terminal open the credentials file and paste your key, replacing the `...`
    - `sudo nano pi-starter-kit/credentials.json`
    - Save and exit
4. Run `sudo nano /etc/rc.local`
5. Change our script path to `sudo python /home/pi/pi-starter-kit/05_cloud/main.py.py &` BEFORE `exit0`
6. Save and exit the file. Reboot the pi by running `sudo reboot`.
4. After a few minutes, press the button and if the light flashes 4 times then it worked!
7. On a separate computer go to [https://dashboard.hologram.io/?drawer=full](https://dashboard.hologram.io/?drawer=full) to see the data from the device!
8. After you verify the script and hardware works, open `main.py` to inspect what we're doing.
    - `cat pi-starter-kit/05_cloud/main.py`
