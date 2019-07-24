# -*- coding:utf-8 -*-
# Author:D.Gray
import pika,sys
connacton = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connacton.channel()

channel.exchange_declare(exchange='topic_logs',exchange_type='topic')

result = channel.queue_declare(exclusive=True)  #随机生成一个队列名

queue_name = result.method.queue

serverities = sys.argv[1:]

if not serverities:
    sys.stderr.write('生产者要定义一个日志级别')
    sys.exit()

print('日志级别：',serverities)
for serverity in serverities:
    channel.queue_bind(exchange='topic_logs',queue=queue_name,routing_key=serverity)


def callback(ch,method,properties,body):
    print('消费者收到消息:',body.decode())

channel.basic_consume(callback,queue=queue_name)

print('现在开始收消息'.center(50,'-'))
channel.start_consuming()