from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark import SparkConf


spark = SparkSession \
                .builder \
                .appName("TESTING_SPARK_") \
                .getOrCreate()

print(spark)

stream_test = spark \
                .readStream \
                .format("kafka") \
                .option("kafka.bootstrap.servers", "localhost:9092") \
                .option("kafka.group.id", "TestGroup") \
                .option("kafka.session.timeout.ms", 1000) \
                .option("subscribe", "horse-coordinates") \
                .option("startingOffset", "earliest") \
                .load()

stream_test.select("value")

query = stream_test \
    .writeStream \
    .outputMode("update") \
    .format("console") \
    .start()

# raw = spark.sql("select * from `kafka-streaming-messages`")
# raw.show()

query.awaitTermination()

# spark = SparkSession \
#         .builder \
#         .appName("StreamingDataPractice0") \
#         .master("local") \
#         .getOrCreate()

# conf = SparkConf().\
#             setAppName("phdata-ddos-detection").\
#             setMaster('local[*]').\
#             set('spark.driver.maxResultSize', '0').\
#             set('spark.jars.packages','io.delta:delta-core_2.11:0.3.0,org.apache.spark:spark-streaming-kafka-0-10_2.11:2.4.3,org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.3')
# org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.1

# query = "SELECT value FROM tmp_table"


# spark.sql(query) \
#     .select("value") \
#     .writeStream \
#     .outputMode("update") \
#     .trigger(processingTime='10 seconds') \
#     .start() \
#     .awaitTermination()
# tmp_stream_info = stream_test \
# .writeStream \
# .outputMode("update") \
# .option("truncate", "false")\
# .format("console") \
# .start()



# tmp_stream_info.awaitTermination()

# stream_test.printSchema() 
# stream_test.isStreaming              .option("kafka.client.id", "clienttest") \
                # .option("kafka.session.timeout.ms",10000 ) \
# stream_test.select("value")

# ./bin/spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.1 ...
# docker exec -it spark \
# spark-submit \
# --packages "org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.0" \
# --master "spark://172.18.0.10:7077" \
# --class Streaming \
# --conf spark.jars.ivy=/opt/bitnami/spark/ivy \
# ivy/spark-streaming-with-kafka_2.12-1.0.jar