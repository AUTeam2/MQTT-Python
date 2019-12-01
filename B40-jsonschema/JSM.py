import time

import paho.mqtt.client as mqtt

import jsonschematest as jss

"""
JSM testscript

JSM tests jsonschematest together with PahoMqttTest.
Writes a json-file, reads the json-file, checks the data against a schema,
sends the data to auteam2.mooo.com receives the response, validates it again.
See B35 - PahoMqttTest.py and and jsonschematest.py documentation on the code.
"""

schemafile = "json.schema"
badpackage = "bad.json"
goodpackage = "good.json"

# Testdata formatted as json(no errors)
test_data1 = {"protocolVersion": 1.0, "sentBy": "Tommy", "msgType": "Command", "commandList": "Run, along!",
              "statusCode": "I'm OK!", "parameterObj": {}, "dataObj": {}, "embeddedFileFormat": "", "embeddedFile": ""}
# Testdata formatted as json(with error in dataObj - it is formatted as a string and sentBy is missing)
test_data2 = {"protocolVersion": 2.0, "msgType": "Dos", "commandList": "Go away!",
              "statusCode": "I'm not OK!", "parameterObj": {}, "dataObj": "", "embeddedFileFormat": "",
              "embeddedFile": ""}

schema = jss.load_schema(schemafile)
jss.write_jsonfile(goodpackage, test_data1)
jss.write_jsonfile(badpackage, test_data2)
data = jss.read_jsonfile(goodpackage)
jss.validering(data, schema)


def on_log(client, userdata, level, buf):
    print("log: " + buf)


def on_connect(client, userdata, falgs, rc):
    if rc == 0:
        print("Connected OK")
    else:
        print("Bad connection The return code is: ", rc)


def on_disconnect(client, userdata, flags, rc=0):
    print("DisConnected result code " + str(rc))


def on_message(client, userdata, msg):
    topic = msg.topic
    m_decode = str(msg.payload.decode("utf-8", "ignore"))
    print("message received", m_decode)
    jss.validering(jss.read_jsonstr(m_decode), schema)


# Janus test server get named broker
# broker = '119.74.164.55'
broker = 'auteam2.mooo.com'
# Create new instance
client = mqtt.Client("Testpython")
client.username_pw_set("team2", "team2")
client.on_connect = on_connect
client.on_disconnect = on_disconnect
# client.on_log = on_log
client.on_message = on_message
print("Connecting to broker ", broker)
# Connecting to broker
client.connect(broker)
# starting loop for the callback to be processed
client.loop_start()
client.subscribe("tester//42")
client.publish("tester//42", str(jss.write_jsonstr(data)))

# w8 5 sec
time.sleep(5)
# ending loop
client.loop_stop()
# Disconnect from server
client.disconnect()
