import mysql.connector
import uuid
import datetime
import traceback

def connect_database():
   """_summary_

   Returns:
       _type_: The cursor and the connection object
   """   
   conn = mysql.connector.connect(
      user='application', password='&0Dwr6VOj8O&lttzzpIXmvik', host='80.208.228.90', database='iot_db')
   
   return conn.cursor(), conn

def send_sensor_data(device_UUID, timestamp, temperature, humidity, batteryv, longitude, latitude):
   """_summary_

   Args:
       device_UUID (_type_): _description_
       timestamp (_type_): _description_
       temperature (_type_): _description_
       humidity (_type_): _description_
       batteryv (_type_): _description_
       longitude (_type_): _description_
       latitude (_type_): _description_
   """   
   record_UUID = uuid.uuid4().hex
   timestamp = datetime.datetime.fromtimestamp(timestamp)
   cursor, conn = connect_database()
   
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
   
def get_device_uuid():
   """_summary_

   Returns:
       _type_: List of device name strings
   """   
   cursor, conn = connect_database()
   euid_list = []
   
   select_stmt = "SELECT recordUUID FROM Device"
   
   try:
      # Executing the SQL command
      cursor.execute(select_stmt)
      result = cursor.fetchall()
      euid_list = [e[0] for e in result]
   except Exception:
      traceback.print_exc()
      conn.rollback()
   conn.close()
   return euid_list
   
   