import psutil
import os
from influxdb import InfluxDBClient
import time,math,random

p1=psutil.Process(os.getpid())

from influxdb import InfluxDBClient
import time,math,random
while True:
	a = psutil.virtual_memory().perecent

	b = psutil.cpu_percent(interval=1.0)

	json_bosy = [
		{
			"measurement":"cpu_load_short",
			"tags":{
				"host": "server01",
				"region": "us-west"
			},
			"fields":{
				"cpu":b,
				"mem":a
			}
		}
	]
	client = InfluxDBClient('localhost',8086,'root','root','xxyyxx')
	client.create_database('xxyyxx',if_not_exists=False)
	client.write_points(json_bosy)
	time.sleep(2)