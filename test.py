from APIConnections import get_device_uuid, send_sensor_data

send_sensor_data("UUID", 122323, 23, 23, 23, 42, 42)
print(get_device_uuid())