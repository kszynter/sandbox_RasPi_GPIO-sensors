# sandbox_RasPi_GPIO-sensors
Scripts for:
- reading multiple DS18B20 temperature sensors
- reading a GL5528 light sensor

The code is based on:
https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing/software

Modified it to read multiple sensors.

Remember to add an entry to /boot/config.txt and reboot. When using GPIO PIN 2 it is:
dtoverlay=w1-gpio,gpiopin=2
