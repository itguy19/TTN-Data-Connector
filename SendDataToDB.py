import mysql.connector
import uuid

def send_sensor_data(device_UUID, timestamp, temperature, humidity, batteryv, longitude, latitude): 
   record_UUID = uuid.uuid4().hex
   
   conn = mysql.connector.connect(
      user='application', password='&0Dwr6VOj8O&lttzzpIXmvik', host='80.208.228.90', database='iot_db')

   cursor = conn.cursor()
   
   insert_stmt = (
      "INSERT INTO record(recordUUID, deviceUUID, timestamp, temperature, humidity, batteryv)"
      "VALUES (%s, %s, %s, %s, %s)"
   )
   data = (record_UUID, device_UUID, timestamp, temperature, humidity, batteryv)

   try:
      # Executing the SQL command
      cursor.execute(insert_stmt, data)
      conn.commit()
   except:
      conn.rollback()
   conn.close()