#-*-coding:utf-8 -*-
# Author: D.Gray
import os,sys,paramiko,threading,time,json
from conf import setting
class MyFabric(object):
    def __init__(self):
        self.run = self.run()


    def run(self):
        text = """
                    欢迎来到Fabric主机管理界面
                        1.创建主机
                        2.删除主机
                        3.自动激活所有主机
                        4.开始远程操控
                        5.退出程序
            """
        while True:
            print(text)
            choose = input("请输入您的选择>>>:").strip()
            #print(type(choose))
            self.dic = {
                '1':self.new_host,
                '2':self.delect_host,
                '3':self.auto_host,
                '4':self.action_host,
                '5':self.exit
            }
            if choose in self.dic:
                self.dic[choose]()
            else:
                print("请输入有效操作")

    def new_host(self):
        print('in the new_host')
        self.db_path = setting.HOST_NAME_PATH
        while True:
            name = input('请输入登录名称(输入n=返回上级)>>>：').strip()
            name_path = os.path.join(self.db_path,'%s.json'%(name))
            #print(name_path)
            if os.path.exists(name_path):
                print('登录名称已存在')
                continue
            if name == 'n':
                return
            hostname = input('请输入主机名(输入n=返回上级)>>>：').strip()
            if hostname == 'n':
                return
            port = input('请输入端口号(输入n=返回上级)>>>：').strip()
            if port.isdigit():
                port = int(port)
            else:
                print('端口号必须是整数')
                return
            if port == 'n':
                return
            username = input('请输入用户名(输入n=返回上级)>>>：').strip()
            if username == 'n':
                return
            password = input('请输入密码(输入n=返回上级)>>>：').strip()
            if password == 'n':
                return
            newhost_dic = {
                "name":name,
                "hostname":hostname,
                "username":username,
                "port":port,
                "password":password,
                "status": 0
            }
            mesag = '''\033[33;1m
                                            请确认录入信息：\n%s:
                    友情提示：请务必确保信息填写无误否则将无法正常进行管理登录操作！！！
            \033[0m'''%newhost_dic
            print(mesag)
            choose = input("开人确认录入信息（y/n）？:")
            if choose == 'n':
                print('信息确认失败将重新录入:')
                return
            elif choose == 'y':
                if os.path.isdir(name_path) == False:
                    with open(name_path,'w') as fw:
                        json.dump(newhost_dic,fw,indent=4)
                    print('信息载入完成')
                    break
                else:
                    print('已存在改文件')
            else:
                print('输入有误请重新输入')


    def delect_host(self):
        print('in the delect_host')
        host_dic = self.add_host()
        host_list = []
        for index,values in enumerate(host_dic.values()):
            host_list.append(values['hostname'])
            print('当前已存在主机名列表如下：')
            print('%s-主机名：%s' % (index + 1, values['hostname']))
        if len(host_list) != 0:
            choose = input("请输入你想删除的主机索引(输入n=返回上级)：")
            if choose =='n':
                print('取消删除主机名')
                return
            if choose.isdigit():
                choose = int(choose)
                if len(host_list) != 0:
                    if choose <= len(host_list):
                        # host_name(文件名称)
                        #  list(host_dic.keys())[choose-1](用户输入索引对应的主机名,也就是key)
                        host_name = list(host_dic.keys())[choose-1]
                        db_path = os.path.join(setting.HOST_NAME_PATH, host_name)
                        os.remove(db_path)
                        print('删除成功')
                    else:
                        print('输入超出索引范围')
                else:
                    print('当前主机索引不能在删除')
            else:
                print('请输入有效索引')
        else:
            print('当前已存在主机名列表为空请先创建主机')


    def add_host(self):
        '''
        获取db文件夹中json文件中的主机名
        :return:将已获取到的主机名列表作为参数返回
        '''
        names_list = [] #定义一个文件名列表
        dic_list = []  #定义一个文件字典列表
        db_dic = {} #定义一个db文件内容字典
        db_path = setting.HOST_NAME_PATH
        ol = os.listdir(db_path)
        for i in ol:
            if i.endswith('.json'): #只获取后缀名为.json文件的信息
                json_path = os.path.join(db_path,i)
                with open(json_path,'r') as f:
                    fr = f.read()
                    fd = eval(fr)
                    dic_list.append(fd)
                    names_list.append(i)
        db_dic = dict(zip(names_list,dic_list))
        #print(db_dic)
        return db_dic


    def auto_host(self):
        print('in the auto_host')
        text = """\033[32;1m
                    警告！程序准备开启多线程模式激活主机，请确保：
                    1，远程服务器处于开启状态
                    2，DNS或本地hosts映射能够解析远程服务器主机名
            \033[0m"""
        while True:
            print(text)
            host_dic = self.add_host()
            host_list = []
            for index,values in enumerate(host_dic.values()):
                host_list.append(values['hostname'])
                print('当前已存在主机名列表如下：')
                print('%s-主机名：%s' % (index + 1,values['hostname']))
            if len(host_list) != 0:
                choose = input("\033[33;1m是否开始确认激活主机（y/n）？:\033[0m")
                if choose == 'n':
                    print('已取消激活')
                    return
                elif choose == 'y':
                    for item in host_dic.values():
                        print('程序开始激活主机请稍后...')
                        time.sleep(1)
                        dic = item
                        t = threading.Thread(target=self.auto_action,args=(dic,))
                        t.setDaemon(True)
                        t.start()
                        while threading.activeCount() != 1:
                            pass
                    print('当前活跃线程个数：', threading.activeCount())
                    break
                else:
                    print('输入有误请重新输入')
                    continue
            else:
                print('请先创建主机')
                return

    def auto_action(self,dic):
        ssh  = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(hostname=dic['hostname'],port=dic['port'],username=dic['username'],password=dic['password'])
        except Exception as e:
            print('\033[31;1m主机-%s 尝试连接失败：\033[0m\n%s'%(dic['hostname'],e))
            dic['status'] = 2
            self.update_dic(dic)
        else:
            stdin, stdou, stdeer = ssh.exec_command('who')
            result = stdou.read()
            print('\033[32;1m主机-%s 尝试连接激活成功\033[0m\n%s' % (dic['hostname'],result.decode()))
            dic['status'] = 1
            self.update_dic(dic)
        finally:
            ssh.close()

    def update_dic(self,dic):
        db_path = os.path.join(setting.HOST_NAME_PATH,'%s.json'%(dic['name']))
        with open(db_path,'w') as f:
            json.dump(dic,f,indent=4)
            return True

    def action_host(self):
        print('in the action_host')
        auto_dic = self.add_host().values()
        auto_list = []
        action_list = []
        for values in auto_dic:
            if values['status'] == 1:
                auto_list.append(values)
                for index,info in enumerate(auto_list):
                    print('已激活的主机如下：\n%s-主机名：%s'%(index+1,info['hostname']))
                    choose = input('请选择项要控制的主机序号(输入n返回上一级)>>>:').strip()
                if choose.isdigit():
                    if choose <= index:
                        chooses = list(set(choose))  #去重多选
                        print(chooses)
                    else:
                        print('请输入有效序号')





    def exit(self):
        #print('in the exit')
        exit('程序退出')
