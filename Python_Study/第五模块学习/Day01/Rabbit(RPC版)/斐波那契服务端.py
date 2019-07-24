# -*- coding:utf-8 -*-
# Author:D.Gray
import pika
import time
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
    print('接收客户端求第[%s]位斐波那契求数'%n)

    response = fib(n)
    #发消息到客户端指定的queue
    channel.basic_publish(exchange='',routing_key=props.reply_to,
                          properties=pika.BasicProperties(correlation_id=props.correlation_id),
                          body = str(response)
                          )
    ch.basic_ack(delivery_tag=method.delivery_tag)  #确认消息被消费

channel.basic_consume(on_response,queue='rpc_queue')  #从rpc_queue一收到消息就调用on_respinse函数处理消息
print("Awaiting RPC requests")
channel.start_consuming()
