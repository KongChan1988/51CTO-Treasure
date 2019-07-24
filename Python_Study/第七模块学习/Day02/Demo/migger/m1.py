# -*- coding:utf-8 -*-
# Author:D.Gray
from django.utils.deprecation import MiddlewareMixin
class Row1(MiddlewareMixin):
    def process_request(self,request):
        print("王森")

    def process_response(self,request,response):
        print("扛把子")
        return response

class Row2(MiddlewareMixin):
    def process_request(self, request):
        print("猪坚强")

    def process_response(self, request, response):
        print("猴呀凡")
        return response

class Row3(MiddlewareMixin):
    def process_request(self, request):
        print("刘东")

    def process_response(self, request, response):
        print("连之类")
        return response