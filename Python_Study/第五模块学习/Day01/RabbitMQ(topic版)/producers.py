# -*- coding:utf-8 -*-
# Author:D.Gray
import pika,sys

connaction = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connaction.channel()

channel.exchange_declare(exchange='topic_logs',exchange_type='topic')

serverity = sys.argv[1] if len(sys.argv) > 1 else 'xxx.info'
mesage = ''.join(sys.argv[2:]) or 'hello_rabbit:topic '

channel.basic_publish(exchange='topic_logs',body=mesage,routing_key=serverity)

print('生产者发送消息:',mesage)

