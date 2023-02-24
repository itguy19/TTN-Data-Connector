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
   
   # Insert new record sql
   insert_stmt = (
      "INSERT INTO Record(recordUUID, deviceUUID, timestamp, temperature, humidity, batteryv)"
      "VALUES (%s, %s, %s, %s, %s, %s)"
   )
   data = (record_UUID, device_UUID, timestamp, temperature, humidity, batteryv)
   
   # Update the position of the device
   update_sql = f"UPDATE Device SET latitude = {latitude}, longitude = {longitude} WHERE deviceUUID = 'eui-a840417ee185f0b5'"

   try:
      # Executing the SQL command
      cursor.execute(insert_stmt, data)
      cursor.execute(update_sql)
      conn.commit()
   except Exception:
      traceback.print_exc()
      conn.rollback()
   conn.close()