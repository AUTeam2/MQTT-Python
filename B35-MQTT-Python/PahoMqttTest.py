import paho.mqtt.client as mqtt
import time

"""
MQTT test script 

The script connects to the broker "auteam2.mooo.com" as the client "Testpython" with username "team2".
Then subscribes to the channel "tester//42" there after publish to channel "tester//42" with a string waits 5 seconds
and disconnects. 
"""


# adding 'callback functions'
def on_log(client, userdata, level, buf):
    """
    Collects login data from client and prints it out
   
    :param client:
    Takes a uniq client instance that is created later
    :param userdata:
    The private user data as set in Client() or user_data_set()
    :param level:
    The level variable gives the severity of the message and will be one of MQTT_LOG_INFO, MQTT_LOG_NOTICE,
    MQTT_LOG_WARNING, MQTT_LOG_ERR, and MQTT_LOG_DEBUG
    :param buf:
    Data related to login used for Debug
    """
    print("log: " + buf)


def on_connect(client, userdata, flags, rc):
    """
    Connects to the broker and prints the result

    :param client:
    Takes a uniq client instance that is created later
    :param userdata:
    The private user data as set in Client() or user_data_set()
    :param falgs:
    Response flags sent by the broker
    :param rc:
    Return code expects a 0 for connects anything else is failed connection
    """
    if rc == 0:
        print("Connected OK")
    else:
        print("Bad connection The return code is: ", rc)


def on_disconnect(client, userdata, flags, rc=0):
    """
    Disconnects from the broker and prints the result

    :param client:
    Takes a uniq client instance that is created later
    :param userdata:
    The private user data as set in Client() or user_data_set()
    :param flags:
    Response flags sent by the broker
    :param rc:
    Return code set to 0
    """
    print("DisConnected result code " + str(rc))


def on_message(client, userdata, msg):
    """
    Receives data from publisher converts it into uft-8 format and prints it

    :param client:
    Takes a uniq instance created later 
    :param userdata:
    The private user data as set in Client() or user_data_set()
    :param msg:
    Takes the data from publisher
    """
    topic = msg.topic
    m_decode = str(msg.payload.decode("utf-8", "ignore"))
    print("message received", m_decode)


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
"""
The client subscribes to a topic can choose level of QoS default is 0
subscribe(topic, qos=0)

"""
client.publish("tester//42", "Test message from team2")
"""
The client publish a message to a topic can choose a level of QoS

This function can take four parameters seen in the brackets:
publish(topic, payload=None, qos=0, retain=False)
The only parameters you must supply are the topic, and the payload.
The payload is the message you want to publish.
"""
# w8 5 sec
time.sleep(5)
# ending loop
client.loop_stop()
# Disconnect from server
client.disconnect()
