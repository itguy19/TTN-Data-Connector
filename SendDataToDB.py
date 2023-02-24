import mysql.connector
import uuid
import datetime
import traceback

def send_sensor_data(device_UUID, timestamp, temperature, humidity, batteryv, longitude, latitude): 
   record_UUID = uuid.uuid4().hex
   timestamp = datetime.datetime.fromtimestamp(timestamp)
   print("Please")
   conn = mysql.connector.connect(
      user='application', password='&0Dwr6VOj8O&lttzzpIXmvik', host='80.208.228.90', database='iot_db')

   cursor = conn.cursor()
   
   insert_stmt = (
      "INSERT INTO Record(recordUUID, deviceUUID, timestamp, temperature, humidity, batteryv)"
      "VALUES (%s, %s, %s, %s, %s, %s)"
   )
   data = (record_UUID, device_UUID, timestamp, temperature, humidity, batteryv)

   try:
      # Executing the SQL command
      cursor.execute(insert_stmt, data)
      conn.commit()
   except Exception:
      traceback.print_exc()
      conn.rollback()
   conn.close()
   
send_sensor_data("eui-a840417ee185f0b5", 2352095363, 22.5, 35.7, 3.671, 8.73057686533798, 47.3547373056341)