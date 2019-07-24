#-*- Coding:utf-8 -*-
# Author: D.Gray
class Flight(object):
    def __init__(self,flight_name):
         self.flight_name = flight_name

    def cacke_status(self):
        print("检查了%s航班信息"%self.flight_name)
        return 2

    @property
    def flight_status(self):
        status = self.cacke_status()
        if status == 0:
            print("flight got canceled...")
        elif status == 1:
            print("flight is arrived...")
        elif status == 2:
            print("flight has departured already...")
        else:
            print("cannot confirm the flight status...,please check later")

    @flight_status.setter
    def flight_status(self,status):
        print("新加状态:%s"%status)

f = Flight("CA980")
f.flight_status