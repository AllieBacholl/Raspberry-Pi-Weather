# Deletes data that is two months old from temperatures and resets the auto increment id. 

import time
import MySQLdb as mdb
import datetime
from dateutil.relativedelta import relativedelta

databaseUsername="root" #YOUR MYSQL USERNAME, USUALLY ROOT
databasePassword="password" #YOUR MYSQL PASSWORD
databaseName="WordpressDB" #do not change unless you named the Wordpress database with some other name

con=mdb.connect("localhost", databaseUsername, databasePassword, databaseName)

def selectOldData():

    currentDate=datetime.datetime.now().date()
    oldDate=currentDate + relativedelta(months=-3)

    with con:
        cur=con.cursor()

        cur.execute("SELECT * FROM temperatures")
        data = cur.fetchall()
        oldData = []

        for x in data:

            if x[4] < oldDate:
                oldData.append(x)

        for x in oldData:
            id = x[0]
            cur.execute("DELETE FROM temperatures WHERE id = %s",(x[0],))

        cur.execute("SET @count=0")
        cur.execute("UPDATE temperatures SET temperatures.id = @count := @count + 1")
        cur.execute("ALTER TABLE temperatures AUTO_INCREMENT = 1")

        con.commit()
    return "true"

selectOldData()
