'''APIConnections
    Author: Andras Tarlos
    Date: 28/02/23
    Version: 1.0

Description:

This Python script sends and retrieves data to an API (Application Programming Interface). The information
is sent via the HTTP protocol to the server.

'''

import requests
import json
import traceback

def send_sensor_data(device_UUID, timestamp, temperature, humidity, batteryv, longitude, latitude):
   """_summary_

   Args:
       device_UUID (_type_): A universal unique identifier for a device
       timestamp (_type_): A UNIX timestamp that shows the time when the data was sent
       temperature (_type_): Temperature in Celsius
       humidity (_type_): Humidity
       batteryv (_type_): The current battery voltage
       longitude (_type_): Coordinate longitude
       latitude (_type_): Coordinate latitude
   """
   json_dict = {
      "deviceUUID": device_UUID,
      "timestamp": timestamp,
      "temperature": temperature,
      "humidity": humidity,
      "batteryv": batteryv,
      "longitude": longitude,
      "latitude": latitude
   }
   
   json_object = json.dumps(json_dict)
   try:
      status = requests.post("http://80.208.228.90:8080/record/insert", json = json_object)
   except Exception:
      traceback.print_exc()
   
def get_device_uuid():
   """_summary_

   Returns:
       _type_: A list of device name strings
   """
   try:
      result = requests.get("http://80.208.228.90:8080/device/list")
   except Exception:
      traceback.print_exc()
   return [x["deviceUUID"] for x in result.json()]
   
   