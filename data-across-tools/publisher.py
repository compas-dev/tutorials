import time

from compas_eve import Message
from compas_eve import Publisher
from compas_eve import Topic
from compas_eve.mqtt import MqttTransport

topic = Topic("/compas_eve/hello_world/", Message)
tx = MqttTransport("broker.hivemq.com")

publisher = Publisher(topic, transport=tx)

for i in range(100):
    msg = Message(text=f"Hello world #{i} from VS Code")
    print(f"Publishing message: {msg.text}")
    publisher.publish(msg)
    time.sleep(1)
