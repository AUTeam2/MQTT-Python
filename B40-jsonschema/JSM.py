import jsonschematest
import PahoMqttTest
import paho.mqtt.client as mqtt
import json


testData1 = jsonschematest.data1
testData2 = jsonschematest.data2

schemafile = "json.schema"
badpackage = "bad.json"
goodpackage = "good.json"


print(testData1)

schema = jsonschematest.loadschema(schemafile)
jsonschematest.writeToJsonFile(goodpackage, testData1)
data = jsonschematest.readFromJsonFile(goodpackage)
jsonschematest.validering(data, schema)



#broker = '119.74.164.55'
PahoMqttTest.broker = 'auteam2.mooo.com'
# Create new instance
PahoMqttTest.client = mqtt.Client("Testpython")
PahoMqttTest.client.username_pw_set("team2", "team2")
PahoMqttTest.client.on_connect = PahoMqttTest.on_connect
PahoMqttTest.client.on_disconnect = PahoMqttTest.on_disconnect
# client.on_log = on_log
PahoMqttTest.client.on_message = PahoMqttTest.on_message
print("Connecting to broker ", PahoMqttTest.broker)
# Connecting to broker
PahoMqttTest.client.connect(PahoMqttTest.broker)
# starting loop for the callback to be processed
PahoMqttTest.client.loop_start()
PahoMqttTest.client.subscribe("tester//42")
"""
The client subscribes to a topic can choose level of QoS default is 0
subscribe(topic, qos=0)

"""
PahoMqttTest.client.publish("tester//42", json.dumps(data))
"""
The client publish a message to a topic can choose a level of QoS

This function can take four parameters seen in the brackets:
publish(topic, payload=None, qos=0, retain=False)
The only parameters you must supply are the topic, and the payload.
The payload is the message you want to publish.
"""
# w8 5 sec
PahoMqttTest.time.sleep(5)
# ending loop
PahoMqttTest.client.loop_stop()
# Disconnect from server
PahoMqttTest.client.disconnect()