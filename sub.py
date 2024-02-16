import paho.mqtt.client as paho
import time
from paho import mqtt

client = paho.Client(client_id="", userdata=None,
                    protocol=paho.MQTTv5)
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client.username_pw_set("Favour", "Oyereyi24")
client.connect("6493e4542e944065886b246a56ae7d73.s2.eu.hivemq.cloud", 8883)

def on_message(client, userdata, msg):
    print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

client.subscribe("Test")
client.on_message = on_message
client.loop_forever()