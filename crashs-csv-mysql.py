import csv
import mysql.connector

config = {
  'user': 'root',
  'password': 'Mysql@2018',
  'host': '127.0.0.1',
  'database': 'crashs',
  'raise_on_warnings': True
}

with open('acidentes-2016.csv', 'r') as csvfile:  
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        cnx = mysql.connector.connect(**config)
        x = cnx.cursor()
        try:
           x.execute("""INSERT INTO accidents (date_time_occured, latitude, longitude) VALUES (%s,%s,%s)""",(row['DATA_HORA'],row['LATITUDE'],row['LONGITUDE']))
           cnx.commit()
        except:
           cnx.rollback()
        x.close()
        cnx.close()