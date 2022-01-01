import paho.mqtt.client as pmqtt
import json
import db

HOST = "127.0.0.1"
PORT = 1883

client_id = "Device_node_System_Server"
client = pmqtt.Client(client_id)  # 设置mqtt初始化


def on_connect(client, userdata, flags, rc):
    print("Connected with result code" + str(rc))
    client.subscribe("Lab/#")


def on_message(client, userdata, msg):
    print("topic:" + msg.topic + "\r\n" + "msg:" +
          str(msg.payload.decode('utf-8')))
    MQTT_listen(msg.topic, str(msg.payload.decode('utf-8')))


def on_subscribe(client, userdata, mid, granted_qos):
    print("On Subscribed: qos = %d" % granted_qos)


def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpect disconnection %s" % rc)


def MQTT_init():
    client.username_pw_set("admin", "public")  # 设置mqtt账户
    client.on_connect = on_connect  # 设置mqtt连接
    client.on_message = on_message  # 设置mqtt获取信息
    client.on_subscribe = on_subscribe  # 设置mqtt qos
    client.on_disconnect = on_disconnect  # 设置mqtt断开链接
    client.connect(HOST, PORT, 60)  # qtt开始连接
    # client.publish("Lab/send", payload=param, qos=0)  # mqtt发布消息
    print("MQTT init finished!")
    client.loop_forever()  # 循环


def MQTT_listen(topic, msgstr):
    # Lab/*loacl*/*id*/RX&TX
    if (topic.split('/')[-1] == 'RX'):
        if (topic.split('/')[1] == '415'):
            print("Receive data from <" + topic.split('/')[1] + ">\r\n" +
                  "Device id is <" + topic.split('/')[2] + ">\r\n")
            parse = json.loads(msgstr)
            MQTT_save_into_db(parse)

    # print("listening....")


def MQTT_save_into_db(dev):
    print(dev)
    db.update_all(dev['uuid'], dev['local'], dev['state'], dev['vlotage'], dev['current'], dev['apower'], dev['aelectricity'], dev['powerfactor'], str(dev['analysis']), dev['user']['name'], dev['user']['id'])


def MQTT_publish(topic, msg, qoslevel):
    client.publish(topic, payload=msg, qos=qoslevel)


# 捏信息
data = {"code": 0, "state": 0}
param = json.dumps(data)
