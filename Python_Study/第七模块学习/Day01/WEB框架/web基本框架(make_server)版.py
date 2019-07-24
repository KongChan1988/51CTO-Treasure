#-*-coding:utf-8 -*-
# Author: D.Gray
from wsgiref.simple_server import make_server
def handle_index():
    return ['<h1>Hello Index</h1>'.encode('utf-8'), ]

def handle_date():
    return ['<h1>Hello Date</h1>'.encode('utf-8'), ]

def RunServer(environ,start_response):
    #environ  客户端发来的所有数据
    #start_response  封装要返回给用户的数据 响应头状态
    start_response("200 OK",[('Content-Type','text/html')])
    #     python3里需把字符串转化成字节  return ['<h1>Hello Web</h1>'.encode('utf-8'),]
    #     python2里用  return '<h1>Hello Web</h1>'    就行
    # return ['<h1>Hello Web</h1>'.encode('utf-8'),]
    use_url = environ["PATH_INFO"]
    print(use_url)
    if use_url == "/index":
        return handle_index()
    elif use_url == "/date":
        return handle_date()
    else:
        return ['<h1>404</h1>'.encode('utf-8'), ]

if __name__ == '__main__':
    httpd = make_server("",8001,RunServer)
    print("Server HTTP on port 8001")
    httpd.serve_forever()