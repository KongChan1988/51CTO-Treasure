# -*- coding:utf-8 -*-
# Author:D.Gray
import pika,uuid,time
from conf import setting
class MyRpc(object):
    def __init__(self):
        self.connaction = pika.BlockingConnection(pika.ConnectionParameters(setting.LOCAL_HOST))
        self.channel = self.connaction.channel()
        self.result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = self.result.method.queue
        self.channel.basic_consume(self.on_response,no_ack=True,queue=self.callback_queue)

    def on_response(self,ch,method,props,body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self,cmd):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',routing_key='rpc_queue',
                                   properties=pika.BasicProperties(reply_to=self.callback_queue,
                                                                   correlation_id= self.corr_id
                                                                   ),
                                   body=str(cmd)
                                   )

        while self.response is None:
            self.connaction.process_data_events()
        task_id = self.corr_id
        res = self.response.decode()
        list = []
        list.append(res)
        list.append(cmd)
        tmp_dic[task_id] = res
        print('task_id:[%s] \t cmd:[%s] \t res:[%s]'%(task_id,cmd,res))
        return task_id,res

    def run(self,*args):
        cmd = args[0]
        #print('in the rum:',cmd)
        try:
            self.call(cmd[1])
        except IndexError as e:
            print('数组越界:',e)
            self.help()

    def check_all(self,*args):
        if len(tmp_dic) == 0:
            print('暂无任务ID')
        else:
            print('任务ID列表：')
            for index,key in enumerate(tmp_dic.keys()):
                print('%s\t task_id:【%s】\t cmd:【%s】\t host:【%s】'%(index+1,key,
                                                                  tmp_dic[key][1],tmp_dic[key][2]))

    def check_task(self,*args):
        cmd = args[0]
        #print('in the check_task:',cmd)
        try:
            print('任务ID[%s]的执行结果：%s'%(cmd[1],tmp_dic[cmd[1]]))
            del tmp_dic[cmd[1]]
        except IndexError as e:
            print('数组越界:', e)
            self.help()
        except KeyError as e:
            print('无效的任务ID：',e)


    def help(self,*args):
        meg = '''\033[32;1m
        run "df -h" --hosts 127.0.0.1 192.168.84.66：操作指令格式 
        check_task 54385061-aa3a-400f-8a21-2be368e66493：查看任务ID执行结果
        check_all：查看所有任务ID
        \033[0m'''
        print(meg)

    def start(self,cmd):
        if hasattr(self,cmd[0]):
            func = getattr(self,cmd[0])
            func(cmd)
        else:
            print('请输入有效操作指令')

rpc_client = MyRpc()
tmp_dic = {}
while True:
    cmd_input = input('请输入操作指令>>>:').strip().split()
    if len(cmd_input) == 0:continue
    else:
        rpc_client.start(cmd_input)


