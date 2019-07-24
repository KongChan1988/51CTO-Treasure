# -*- coding:utf-8 -*-
# Author:D.Gray
import pika,uuid,time
class FibonacciRpcClient(object):
    def __init__(self):
        self.connaction = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connaction.channel()
        self.result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = self.result.method.queue  #定义一个随机queue
        # 客户端一收到消息就调用on_response函数
        self.channel.basic_consume(self.on_response,no_ack=True,queue=self.callback_queue)

    def on_response(self,ch,method,props,body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self,n):
        self.response = None
        self.corr_id = str(uuid.uuid4())        #设置一个回调通道ID

        self.channel.publish(exchange='',routing_key='rpc_queue',   #发送消息到rpc_queue,
                             properties=pika.BasicProperties(
                                 # reply_to设置一个服务端发送回调消息到的队列，客户端就从这个队列中监听消息
                                 reply_to=self.callback_queue,
                                correlation_id = self.corr_id
                             ),
                             body=str(n))  #交给接收端的参数

        while self.response is None:    #实时监听队列消息
            self.connaction.process_data_events()
            print('no message...')
            time.sleep(1)
        return int(self.response)

rpc_client = FibonacciRpcClient()
response = rpc_client.call(8)    #response就是收到服务端传来的求值结果
print('斐波那契第8位数是:%s'%response)

