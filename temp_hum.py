from machine import Pin
from time import sleep
import dht

sensor = dht.DHT22(Pin(2))

while True:
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    print(f"teplota: {temp}  Vlhkost: {hum}")
    sleep(2)