# -*- coding:utf-8 -*-
# Author:D.Gray
'''
rabbitmq宕机或断开 队列和队列消息都会清除
durable=True：只持续化队列，队列消息会清除
properties=pika.BasicProperties(
                          delivery_mode=2           #队列消息持续化
                      )

注：队列未持续化，只持续化队列消息  rabbitmq宕机或断开 队列和队列消息都会清除
'''
import pika

connaction = pika.BlockingConnection(pika.ConnectionParameters('localhost'))  #建立socket连接

channel = connaction.channel()

channel.queue_declare(queue='hello2',durable=True)

channel.basic_publish(exchange='',
                      routing_key='hello2',
                      body='hello queue',
                      properties=pika.BasicProperties(delivery_mode=2)  #队列消息持续化
                      )

print('生产者发送消息:','hello queue')
connaction.close()