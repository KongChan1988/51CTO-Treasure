# -*- coding:utf-8 -*-
# Author:D.Gray
import pika
connaction = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connaction.channel()
channel.queue_declare(queue='rpc_queue')

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def on_response(ch,method,props,body):
    n = int(body)
    print('接收客户端传来参数[%s]'%n)
    response = fib(n)

    channel.basic_publish(exchange='',routing_key=props.reply_to,
                          properties=pika.BasicProperties(correlation_id=props.correlation_id),
                          body=str(response)
                          )
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(on_response,queue='rpc_queue')
print('等待客户端传来参数')
channel.start_consuming()



