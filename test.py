from APIConnections import get_device_uuid, send_sensor_data
import calendar
import time

current_GMT = time.gmtime()
ts = calendar.timegm(current_GMT)
send_sensor_data(get_device_uuid()[0], 1678035029 * 1000, 23, 23, 23, 43, 43)