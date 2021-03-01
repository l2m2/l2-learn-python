import paho.mqtt.subscribe as subscribe

topic = "iot_s/use/062105202510030/Kinco/fmt/json"


def on_message_print(client, userdata, message):
  print("%s %s" % (message.topic, message.payload))


subscribe.callback(
  on_message_print,
  topic,
  hostname="139.196.104.13",
  port=1883,
)
