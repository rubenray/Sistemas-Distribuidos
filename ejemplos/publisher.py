import paho.mqtt.client as mqtt
import time

client = mqtt.Client()
client.connect("localhost", 1883)

while True:
    client.publish("curso/mqtt","mensaje desde raspberry pi")
    print("Publicado")
    time.sleep(1)
