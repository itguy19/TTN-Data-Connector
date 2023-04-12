'''APIConnections
    Author: Andras Tarlos
    Date: 28/02/23
    Version: 1.0

Description:

This Python script sends and retrieves data to an API (Application Programming Interface). The information
is sent via the HTTP protocol to the server.

'''

import requests
from requests.auth import HTTPBasicAuth
import traceback
from ReadData import read_iot_api_key

IOT_API_KEY = read_iot_api_key()


def send_sensor_data(device_UUID, timestamp, temperature, humidity, batteryv, longitude, latitude):
    """_summary_

    Args:
        device_UUID (str): A universal unique identifier for a device
        timestamp (str): A UNIX timestamp that shows the time when the data was sent
        temperature (float): Temperature in Celsius
        humidity (float): Humidity
        batteryv (float): The current battery voltage
        longitude (float): Coordinate longitude
        latitude (float): Coordinate latitude
        key (str): The IOT-API access key
    """

    try:
        requests.post("http://80.208.228.90:8080/record/insert", json={
            "deviceUUID": device_UUID,
            "temperature": temperature,
            "humidity": humidity,
            "batteryv": batteryv,
            "latitude": latitude,
            "longitude": longitude,
            "timestamp": timestamp,
            "key": IOT_API_KEY})
    except Exception:
        traceback.print_exc()


def get_device_uuid():
    """_summary_

    Returns:
        list: A list of device name strings
    """
    try:
        result = requests.get(
            "http://80.208.228.90:8080/device/list")
    except Exception:
        traceback.print_exc()
    return [x["deviceUUID"] for x in result.json()]
