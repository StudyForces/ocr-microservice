import pika
import sys
from rmq_parameters import *
import json
import requests
import io
from get_text import get_text, preprocessing
import utils

connection = pika.BlockingConnection(pika.ConnectionParameters(HOST))

rmq_channel = connection.channel()
session = requests.Session()

def send(message: str) -> None:
    rmq_channel.basic_publish("", SENDER_QUEUE_NAME, message)

def on_message(channel, method_frame, header_frame, body) -> None:
    data = json.loads(body)
    if (not utils.download_image(session, data["sourceUploadURL"], "temp.png")):
        return None
    rect = data["rect"]
    data.pop("sourceUploadURL")
    data.update([("data", dict().fromkeys(["text"], [""]))])
    data["data"]["text"] = get_text(preprocessing("temp.png", [int(rect["x"]), int(rect["y"]),
                                                               int(rect["width"]), int(rect["height"])]))
    send(json.dumps(data, separators=(',', ':'), ensure_ascii=False))
    rmq_channel.basic_ack(method_frame.delivery_tag)

rmq_channel.basic_consume(CONSUMER_QUEUE_NAME, on_message)

try:
    rmq_channel.start_consuming()
except KeyboardInterrupt:
    rmq_channel.close()
    session.close()
