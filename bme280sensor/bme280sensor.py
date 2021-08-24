import os
import glob
import sys
import re
import time
import subprocess
import MySQLdb as mdb
import datetime
import board
import busio
from adafruit_bme280 import basic as adafruit_bme280

databaseUsername="root" #YOUR MYSQL USERNAME, USUALLY ROOT
databasePassword="Lizzy414" #YOUR MYSQL PASSWORD
databaseName="WordpressDB" #do not change unless you named the Wordpress database with some other name

# Create library object using our Bus I2C port
i2c = busio.I2C(board.SCL, board.SDA)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

# change this to match the location's pressure (hPa) at sea level
bme280.sea_level_pressure = 1008

con=mdb.connect("localhost", databaseUsername, databasePassword, databaseName)
# ---------------------------------

def saveToDatabase():

    currentDate=datetime.datetime.now().date()
    now=datetime.datetime.now()
    midnight=datetime.datetime.combine(now.date(),datetime.time())
    minutes=((now-midnight).seconds)/60 #minutes after midnight, use datead$

    humidity = format(bme280.humidity, ".1f")
    pressure = format(bme280.pressure, ".1f")
    temperature = format(bme280.temperature, ".1F")

    with con:
        cur=con.cursor()

        cur.execute("INSERT INTO temperatures (temperature, humidity, pressure, dateMeasured, hourMeasured) VALUES (%s,%s,%s,%s,%s)",(temperature,humidity,pressure,currentDate, minutes))
        con.commit();

    return "true"

#check if table is created or if we need to create one
try:
    queryFile=open("createTable.sql","r")

    currentDate=datetime.datetime.now().date()

    with con:
        line=queryFile.readline()
        query=""
        while(line!=""):
            query+=line
            line=queryFile.readline()

        cur=con.cursor()
        cur.execute(query)

        #now rename the file, because we do not need to recreate the table everytime this script is run
        queryFile.close()
        os.rename("createTable.sql","createTable.sql.bkp")
        con.commit();

except IOError:
        pass #table has already been created

saveToDatabase()
