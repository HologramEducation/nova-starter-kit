# 00 - Setting up a Raspberry Pi (Headless)

## A. Install OS on SD Card
If you already have Raspbian installed on an OS you can skip to the next section.

1. Download the OS we'll be using - **Raspbian Jessie**
    - Raspbian is a flavor of Debian, made specifically for the Raspberry's ARM architecture
    - Either Lite or Full versions are fine (Lite does not include a desktop UI, not needed for this tut)
    - This is not NOOBS, we'll be using the direct OS download image
    - https://www.raspberrypi.org/downloads/raspbian/
2. Download & install **Etcher** for burning the OS to our SD card
    - https://etcher.io/
3. Insert the SD card into your computer
4. Open Etcher and flash OS to SD
    - Select the downloaded OS zip > Select the SD > FLASH!
    - Should look something like this...<img src="https://s3.amazonaws.com/hologram-devrel-images/%5Bgithub%5Draspi-iot-workshop/00A00.jpg" width="690" height="344">
5. After the flash is completed check if the SD card is mounted, if its not please pull it out and reinsert it.

## B. Configure OS
1. Open a terminal and `cd` into the BOOT drive
    - <img src="https://s3.amazonaws.com/hologram-devrel-images/%5Bgithub%5Draspi-iot-workshop/00B00.png" width="690" height="295">
2. Next we'll enable SSH support and configure WiFi the device will connect to at boot
    - Enable SSH by creating a file --> `$ touch ssh`
    - Enable and configure WiFi --> `sudo nano wpa_supplicant.conf`<img src="https://s3.amazonaws.com/hologram-devrel-images/%5Bgithub%5Draspi-iot-workshop/00B01.png" width="690" height="259">
    - Edit wpa_supplicant.conf with your own wifi ssid and password
      ```
      network={
            ssid="**your-wifi**"
            psk="**your-password**"
            key_mgmt=WPA-PSK
      }
      ```

      - Your terminal should look like this <img src="https://s3.amazonaws.com/hologram-devrel-images/%5Bgithub%5Draspi-iot-workshop/00B02.png" width="690" height="295">
      - **CRTL+X** to exit, **Y** to save, **ENTER** to confirm
3. Eject SD card from your computer and insert into the RaspberryPi

## C. SSH into Device over WiFi
1. Apply power to the Raspberry Pi through its micro USB port
    - Wait a minute for the device to startup
2. Open a terminal and SSH into the new device
    - `$ ssh pi@raspberrypi.local`
    - prompted to enter password: `raspberry`
    - If you do not have the pi on your network you may need to repeat section **1B** above
    - If you have multiple pi devices on your network you'll need to find the local IP address (I like the free Bonjour Browser from http://www.tildesoft.com/)
3. Further RaspberryPi Configuration
    - From the RasPi terminal run `$ sudo raspi-config`<img src="https://s3.amazonaws.com/hologram-devrel-images/%5Bgithub%5Draspi-iot-workshop/00C00.png" width="624" height="500">
    - Expand SD Storage: `7 Advanced Options` --> `A1 Expand Filesystem`
    - Enable I2C to read analog sensors:  `5 Interfacing Options` --> `P5 I2C`
    - Change Password: `1 Change User Password` --> enter new password
    - Change Hostname: `2 Hostname` --> enter new hostname
    - Select `Finish` and approve the reboot
4. SSH back into device with new hostname and password
    - Make sure to put `.local` at the end of your hostname when SSHing.
    - example: `$ ssh pi@myNewHostname.local`
