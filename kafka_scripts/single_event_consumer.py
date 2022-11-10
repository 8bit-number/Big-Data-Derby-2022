from kafka import KafkaConsumer
# import csv
import json
# import msgpack
from kafka.structs import TopicPartition
import time


def receive_data(consumer, topic):
    consumer.subscribe([topic])
    print(consumer.assignment())
    # consumer.assign(
    #     [
    #         TopicPartition(topic, 0),
    #         TopicPartition(topic, 1), 
    #         TopicPartition(topic, 2),
    #         TopicPartition(topic, 3),
    #         TopicPartition(topic, 4),
    #         TopicPartition(topic, 5),
    #         TopicPartition(topic, 6),
    #         TopicPartition(topic, 7),
    #         TopicPartition(topic, 8)
    #     ])

    while True:
        for msg in consumer:
            print(msg)
            print("======")
            # print(json.loads(msg.value.decode()))
            # print(f"Received message from producer: {json.loads(msg.value.decode())}")


if __name__ == "__main__":
    KAFKA_URL = "localhost:29092"
    topic = "horse-coordinates-data"

    consumer = KafkaConsumer(
        bootstrap_servers=KAFKA_URL,
        value_deserializer=lambda m: json.loads(m.decode('ascii')),
        group_id = "test"
    )

    receive_data(consumer, topic)
