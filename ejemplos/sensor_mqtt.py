import Adafruit_DHT as dht
import paho.mqtt.client as mqtt
import time

sensor = dht.DHT22
client = mqtt.Client()
client.connect("localhost",1883)

while True:
    h, t = dht.read_retry(sensor, 4)
    if h is not None and t is not None:
        client.publish("sensor/temperatura", t)
        client.publish("sensor/humedad", h)
        print("T:",t,"H:",h)
    time.sleep(2)
