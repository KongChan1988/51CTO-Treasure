# -*- coding:utf-8 -*-
# Author:D.Gray
import pika
connaction = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connaction.channel()

channel.queue_declare('hello2',durable=True)

def callback(ch,method,properties,body):
    print('消费者收到消息:%s'%body.decode())
    ch.basic_ack(delivery_tag=method.delivery_tag)  #no_ack模式下必须手动给生产者发送消息不然这条消息会一直存在

channel.basic_consume(callback,
                      queue='hello2',
                      #no_ack=True,    #这句话表示无论消费者收没收到消息都不会给生产者发送消息。通常环境下不写。
                      )

print('现在才开始收消息'.center(50,'-'))
channel.start_consuming()