# -*- coding:utf-8 -*-
# Author:D.Gray
import pika

connaction = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connaction.channel()

sel = channel.exchange_declare(exchange='fanout_logs',exchange_type='fanout')

mesage = 'info:hello_rabbit:fanout'

channel.basic_publish(exchange='fanout_logs',body=mesage,routing_key='')

print('生产者发送消息:',mesage)

