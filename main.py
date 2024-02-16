import paho.mqtt.client as paho
from paho import mqtt
def on_connect(client, userdata, flags,  reasonCode, properties):
    if reasonCode==0:
        print("connected")
    else:
        print("Bad connection")


def main():
    client = paho.Client(client_id="", userdata=None,
                        protocol=paho.MQTTv5)
    client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
    client.username_pw_set("Favour", "Oyereyi24")
    client.connect("6493e4542e944065886b246a56ae7d73.s2.eu.hivemq.cloud", 8883)
    client.on_connect = on_connect
    client.publish('Test', payload='This works', qos=0, retain=False)
    client.loop_forever()

if __name__=="__main__":
    main()
