# Raspberry-Pi-Weather

This project was based off of this [tutorial](https://www.raspberryweather.com/). I made some changes so that I could use the [bme280 sensor](https://www.adafruit.com/product/2652) to read humidity and pressure. I used this [tutorial](https://medium.com/initial-state/how-to-build-a-raspberry-pi-temperature-monitor-8c2f70acaea9) to help me set up the sensor. 

The bme280 code will read the temperature, pressure, and humidity from the sensor and add it to a database. Make sure to run the code with Python 3 and not Python 2. The WordPress plugin allows these readings to be displayed as graphs on a website. The bash script can be ran with cron to automate the readings.

Here is a link to the [website](http://alliebacholl.xyz).
