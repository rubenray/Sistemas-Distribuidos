# Practicas de MQTT con Raspberry Pi para sistemas distribuidos

## Introducción

Este curso está diseñado para  aprender **MQTT desde cero utilizando una Raspberry Pi**, con prácticas reales enfocadas en proyectos de IoT.

El material está preparado en formato Markdown para ser colocado directamente en un repositorio de **GitHub**.

---

## 1. ¿Qué es MQTT?

MQTT (Message Queuing Telemetry Transport) es un protocolo de mensajería ligero basado en el patrón **publish/subscribe**, ideal para:

* IoT
* Telemetría
* Sistemas industriales
* Sensores distribuidos

### Características principales

* Ultra ligero
* Usa TCP/IP
* Diseñado para redes inestables
* Ideal para dispositivos de bajo consumo

---

## 2. Requisitos del curso

### Hardware

* Raspberry Pi 3/4/5
* Tarjeta microSD 16GB
* Fuente de alimentación
* Conexión WiFi o Ethernet
* Sensor opcional: DHT22 o cualquier sensor GPIO

### Software

Instalar en Raspberry Pi OS:

```bash
sudo apt update
sudo apt upgrade
sudo apt install mosquitto mosquitto-clients python3 python3-pip
pip3 install paho-mqtt RPi.GPIO Adafruit_DHT
```

---

## 3. Arquitectura MQTT

MQTT tiene tres actores:

* **Broker**: servidor central
* **Publisher**: envía mensajes
* **Subscriber**: recibe mensajes

Ejemplo visual:

```
Sensor → MQTT Publish → [Broker] → MQTT Subscribe → Dashboard
```

---

## 4. Instalación del broker Mosquitto

### Paso 1: Instalar

```bash
sudo apt install mosquitto mosquitto-clients
```

### Paso 2: Habilitar servicio

```bash
sudo systemctl enable mosquitto
sudo systemctl start mosquitto
```

### Paso 3: Verificar

```bash
mosquitto -v
```

---

## 5. Práctica 1: Enviar un mensaje MQTT

### 5.1 Publicar un mensaje

```bash
mosquitto_pub -h localhost -t "test/topic" -m "Hola MQTT"
```

### 5.2 Suscribirse a un topic

```bash
mosquitto_sub -h localhost -t "test/topic"
```

---

## 6. Práctica 2: Publicar mensajes con Python

Crear archivo `publisher.py`:

```python
import paho.mqtt.client as mqtt
import time

client = mqtt.Client()
client.connect("localhost", 1883)

while True:
    client.publish("curso/mqtt", "mensaje desde raspberry pi")
    print("Publicado")
    time.sleep(1)
```

Ejecutar:

```bash
python3 publisher.py
```

---

## 7. Práctica 3: Suscriptor en Python

Crear archivo `subscriber.py`:

```python
import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print(f"Mensaje recibido: {msg.payload.decode()}")

client = mqtt.Client()
client.connect("localhost", 1883)
client.subscribe("curso/mqtt")
client.on_message = on_message
client.loop_forever()
```

Ejecutar:

```bash
python3 subscriber.py
```

---

## 8. Práctica 4: Sensor DHT22 enviando temperatura por MQTT

Código `sensor_mqtt.py`:

```python
import Adafruit_DHT as dht
import paho.mqtt.client as mqtt
import time

sensor = dht.DHT22
broker = "localhost"
client = mqtt.Client()
client.connect(broker, 1883)

while True:
    h, t = dht.read_retry(sensor, 4)
    if h is not None and t is not None:
        client.publish("sensor/temperatura", t)
        client.publish("sensor/humedad", h)
        print("T:", t, "H:", h)
    time.sleep(2)
```

---

## 9. Práctica 5: Dashboard en Node-RED

### Instalación Node-RED

```bash
bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered)
```

### Ejecutar Node-RED

```bash
node-red-start
```

Acceder en navegador:

```
http://localhost:1880
```

### Crear Dashboard

1. Instalar `node-red-dashboard` desde Manage Palette.
2. Crear nodo MQTT-IN.
3. Conectar a broker local.
4. Mostrar datos en gauges y charts.

---

## 10. Proyecto final

Construir un sistema IoT que monitoree temperatura y envíe datos a:

* Node-RED
* Base de datos InfluxDB
* Visualización en Grafana

---

## 11. Recursos recomendados

* Documentación oficial MQTT: [https://mqtt.org](https://mqtt.org)
* Mosquitto: [https://mosquitto.org](https://mosquitto.org)
* Paho MQTT: [https://www.eclipse.org/paho/](https://www.eclipse.org/paho/)
* Node-RED: [https://nodered.org](https://nodered.org)
* Raspberry Pi: [https://www.raspberrypi.com](https://www.raspberrypi.com)

---

## 12. Licencia

Este curso se distribuye bajo licencia MIT para uso educativo y distribución en GitHub.
