from kafka import KafkaProducer
from kafka import KafkaAdminClient
from kafka.admin import NewPartitions
import csv
import json
import time
import msgpack


def send_message(FILE, producer, TOPIC):
    with open("result_.json") as f:
        data_from_file = json.load(f).get("positions")

        pos_count = 0

        for position in data_from_file:

            pos = 0
            # str.encode(i["program_number"])
            #  key=pos.to_bytes(2, 'big')

            for i in position:
                producer.send(topic=TOPIC, partition=pos, value=i)
                pos += 1
                time.sleep(2)
                # break

            break

            # producer.send(topic=TOPIC, key=pos_count, value=data_to_send)
            # pos_count += 1
            # time.sleep(3)


    # producer.flush()

if __name__ == "__main__":

    KAFKA_URL = "localhost:29092"
    FILE = "/Users/atananaiska/Documents/Big Data Derby 2022/info_0.csv"
    TOPIC = "horse-coordinates"
    # try:
    # admin_client = KafkaAdminClient(bootstrap_servers=KAFKA_URL, api_version=(2,0,2))
    # topic_partitions = {}
    # topic_partitions[TOPIC] = NewPartitions(total_count=9)
    # admin_client.create_partitions(topic_partitions)
    # except kafka.errors.InvalidPartitionsError

    producer = KafkaProducer(bootstrap_servers=KAFKA_URL,
                             value_serializer=lambda m: json.dumps(m).encode('ascii'))

    send_message(FILE, producer, TOPIC)


# spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.1 spark_streaming_testing.py