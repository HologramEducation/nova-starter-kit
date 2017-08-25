# Raspberry Pi IoT Workshop

Learn the basics of the Raspberry Pi 3 and Cellular IoT. By the end you'll have a functioning prototype communicating anywhere there is a cell signal, controlling it through a Web App.

### Equipment/Tools Needed:

- [Raspberry Pi 3 or Zero W](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/)
- [MCP3008 Analog-Digital Converter](https://www.adafruit.com/product/856)
- [Breadboard](https://www.adafruit.com/product/239)
- [DHT11 4-pin](https://www.adafruit.com/product/386)
- [LED (any color)](https://www.adafruit.com/product/298)
- [Tactile Button](https://www.adafruit.com/product/367)
- [Photoresistor](https://www.adafruit.com/product/161)
- [220 ohm & 10k ohm Resistors](https://www.adafruit.com/product/2892)
- [M-F Jumper Wires](https://www.adafruit.com/product/1953)
- [M-M Jumper Wires](https://www.adafruit.com/product/1956)
- [USB Cellular Modem](https://hologram.io/store/huawei-ms2131i-usb-cell-modem)
- [Hologram Developer SIM Card](https://hologram.io/devplan/)
- TODO: Add software requirements (stndlib, ide)

### Steps:

You may have a configured Pi available on your network, if you do then skip to Step 01. If not, I'd encourage you to use the setup instructions in Step 00.

**00** - [Headless Raspberry Pi Setup](/00_pi_setup.md)

**01** - [Blink an LED](/01_blink/readme.md)

**02** - [Read a Digital Sensor](/02_digital_sensor/readme.md)

**03** - [Read an Analog Sensor](/03_analog_sensor/readme.md)

**04** - [Trigger with a Button](/04_button/readme.md)

**05** - [Sending Data through WiFi](/05_cloud/readme.md)

**06** - [Sending Data through Cellular](/06_cellular/readme.md)

**07** - Control from a Web App - Coming soon

**BONUS** - Neat things w/cellular
- [Lat/Lon location through cell tower triangulation](https://hologram.io/docs/reference/cloud/python-sdk/#modem-location)
- [Remote SSH tunneling through Hologram SpaceBridge](https://hologram.io/docs/guide/cloud/spacebridge-tunnel/)
