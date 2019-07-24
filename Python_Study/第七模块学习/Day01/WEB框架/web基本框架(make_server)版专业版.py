#-*-coding:utf-8 -*-
# Author: D.Gray
from wsgiref.simple_server import make_server
from Controller import account
USE_URL = {
    '/index':account.handle_index,
    '/date':account.handle_date,
}
def RunServer(environ,start_response):
    #environ  客户端发来的所有数据
    #start_response  封装要返回给用户的数据 响应头状态
    start_response("200 OK",[('Content-Type','text/html')])
    #     python3里需把字符串转化成字节  return ['<h1>Hello Web</h1>'.encode('utf-8'),]
    #     python2里用  return '<h1>Hello Web</h1>'    就行
    use_url = environ["PATH_INFO"]      #获取客户端的url
    print(use_url)
    if use_url in USE_URL:
        #如果客户端地址在USE_URL字典中  则执行相应的func函数否之返回404
        func = USE_URL[use_url]       #func就是客户端IP所对应的函数
        return func()
    else:
        return ['<h1>404</h1>'.encode('utf-8'), ]

if __name__ == '__main__':
    httpd = make_server("",8001,RunServer)
    print("Server HTTP on port 8001")
    httpd.serve_forever()