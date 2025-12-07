import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print("Mensaje recibido:", msg.payload.decode())

client = mqtt.Client()
client.connect("localhost", 1883)
client.subscribe("curso/mqtt")
client.on_message = on_message
client.loop_forever()
