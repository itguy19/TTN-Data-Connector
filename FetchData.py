'''FetchData
    Author: Andras Tarlos
    Date: 24/02/23
    Version: 1.0

Description:

This short script harvests data from TTN (The Things Network). It uses the MQTT protocol to get the data live.
To establish a connection with a device, the application id (APPLICATION_ID), an API Key (API_KEY) and a
unique device id is needed. For security purposes, the connection happens via TLS.

TTN MQTT Documentation: https://www.thethingsindustries.com/docs/integrations/mqtt/
'''

import json
import paho.mqtt.client as mqtt
import calendar
import time
from APIConnections import send_sensor_data, get_device_uuid
from ReadData import read_api_key, read_app_id

APPLICATION_ID = read_app_id()
API_KEY = read_api_key()

TTN_SERVER = "eu1.cloud.thethings.network"
DEVICE_IDS = get_device_uuid()


def on_connect(client, userdata, flags, rc):
    """_summary_
    Shows important information about the connection

    Args:
        client (_type_): the client object
        userdata (_type_): important informations about the user
        flags (_type_): contains information about the session status
        rc (_type_): receive connection code (0 means success)
    """
    print("Connected to ", client._host, "port: ", client._port)
    print("Flags: ", flags, "return code: ", rc)
    # Subscribes to the device to receive data
    for d in DEVICE_IDS:
        TOPIC = f"v3/{APPLICATION_ID}@ttn/devices/{d}/up"
        client.subscribe(TOPIC)


def on_message(client, userdata, msg):
    """_summary_
    The callback for when a PUBLISH message is received from the server.

    Args:
        client (_type_): the client it connects to
        userdata (_type_): data of the user
        msg (_type_): message with relevant information
    """
    # Extract the neccessary information from the json file
    themsg = json.loads(msg.payload.decode("utf-8"))
    humidity = themsg["uplink_message"]["decoded_payload"]["Hum_SHT"]
    batteryv = themsg["uplink_message"]["decoded_payload"]["BatV"]
    temperature = themsg["uplink_message"]["decoded_payload"]["TempC_SHT"]
    current_GMT = time.gmtime()
    timestamp = calendar.timegm(current_GMT) * 1000
    latitude = themsg["uplink_message"]["locations"]["user"]["latitude"]
    longitude = themsg["uplink_message"]["locations"]["user"]["longitude"]
    device_UUID = themsg["end_device_ids"]["device_id"]

    # Send data over to the DB
    send_sensor_data(device_UUID, timestamp, temperature,
                     humidity, batteryv, longitude, latitude)


if __name__ == "__main__":
    """_summary_
    Main function where this system process starts. 
    """
    # Establish connnection
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    # Connect securely via TLS
    client.tls_set()
    client.username_pw_set(APPLICATION_ID, password=API_KEY)
    # Connect on port 8883 with the selected server
    client.connect(TTN_SERVER, 8883, 60)
    client.loop_forever()
