from math import prod
from time import sleep
from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers=['kafka:9092'], group_id='group1')

producer.send('foo', 'This was sent through python')


# input
print("What do you wanna send?")
input = str(input())


if (len(input)!=0):
    producer.send('foo', input)
    sleep(2)