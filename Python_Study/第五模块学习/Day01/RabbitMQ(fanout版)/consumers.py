# -*- coding:utf-8 -*-
# Author:D.Gray
import pika
connacton = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connacton.channel()

channel.exchange_declare(exchange='fanout_logs',exchange_type='fanout')

result = channel.queue_declare(exclusive=True)  #随机生成一个队列名

queue_name = result.method.queue

channel.queue_bind(exchange='fanout_logs',queue=queue_name)

def callback(ch,method,properties,body):
    print('消费者收到消息:',body.decode())

channel.basic_consume(callback,queue=queue_name)

print('现在开始收消息'.center(50,'-'))
channel.start_consuming()