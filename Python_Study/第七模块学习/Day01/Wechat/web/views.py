from django.shortcuts import render,HttpResponse,redirect
import requests
import time,re,json
from bs4 import BeautifulSoup
# Create your views here.
def login(req):
    ctime = time.time()
    #微信向这个地址发送获取二维码请求 base_url接收到请求后会发送给二维码一个参数qcode
    base_url = "https://login.wx.qq.com/jslogin?appid=wx782c26e4c19acffb&redirect_uri=https%3A%2F%2Fwx.qq.com%2Fcgi-bin%2Fmmwebwx-bin%2Fwebwxnewloginpage&fun=new&lang=zh_CN&_={0}"
    result_url = base_url.format(ctime)
    responce = requests.get(
        url=result_url
    )
    print(responce.text)
    v = re.findall('window.QRLogin.code = 200; window.QRLogin.uuid = "(.*)";',responce.text)
    qcode = v[0]
    req.session["qcode"] = qcode
    return render(req,"login.html",{"qcode":qcode})

#https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login?loginicon=true&uuid=QdTrjWxCBg==&tip=1&r=-26088054&_=1537624354611
def check_login(req):
    ret = {"code":408,"data":None}
    tip = req.GET.get("tip")  #获取前端传来的tip参数
    ctime = time.time()
    #url这个地址就是服务器对微信二维码轮询监听是否有人扫码 {0}就是qcode{1}tip判断用户扫码后tip会变0{2}时间戳
    url = "https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login?loginicon=true&uuid={0}&tip={1}&r=-26088054&_={2}"
    base_url = url.format(req.session["qcode"],tip,ctime)
    print('长寻监测用户是否扫码：',base_url)
    r1 = requests.get(
        url=base_url
    )
    # print(r1.text)
    if "window.code=201" in r1.text:
        v = re.findall("window.userAvatar = '(.*)';",r1.text)  #code=201 则表示有人扫码了
        avatar = v[0]       #avatar就是扫码用户的头像信息
        ret["code"] = 201       #已有用户扫码
        ret["data"] = avatar
    elif "window.code=200" in r1.text:
        #用户扫码之后并在手机上点击“确定登录”
        redirect_uri = re.findall('window.redirect_uri="(.*)";',r1.text)[0]
        redirect_url = "{0}&fun=new&version=v2".format(redirect_uri)  #字符串拼接成有效地址
        print('这个redirect_uri可以获取凭证或cookies：', redirect_url)
        r2 = requests.get(url=redirect_url)
        #这个cookie获取用户列表时有用
        req.session["ticket_cookie"] = r2.cookies.get_dict()
        ticket_dict = {}
        soup = BeautifulSoup(r2.text,features="html.parser")
        for item in soup.find(name="error").children:
            ticket_dict[item.name] = item.text
        print("凭证信息：",ticket_dict)  #拿到想要的凭证字典格式
        req.session["ticket_dict"] = ticket_dict    #将凭证放到session里
        ret["code"] = 200           # 用户已经成功登录 code = 200
        req.session["is_login"] = True
    return HttpResponse(json.dumps(ret))

def index(req):
    #判断用户是否已登录
    if not req.session.get("is_login"):
        return redirect('/login/')
    else:
        '''
        往https://wx.qq.com/cgi-bin/mmwebwx-bin/...地址发信息获取基本信息
        发送post请求，根据ticket_dict数据进行构造
        https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxinit?r=173132688&lang=zh_CN&pass_ticket=JaMGEcrn98rND0pb8UVnczadAc07e89OCUBv28usMcvLOkZtjWACOEYjD%252B%252B9Juox
        '''
        base_url = "https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxinit?r=173132688&lang=zh_CN&pass_ticket={0}"
        url = base_url.format(req.session["ticket_dict"]["pass_ticket"])
        print(url)
        #对所需发送的信息做下构造
        form_data = {
            "BaseRequest":{
                "DeviceID":"e008867353964258",
                "Sid":req.session["ticket_dict"]["wxsid"],
                "Skey":req.session["ticket_dict"]["skey"],
                "Uid": req.session["ticket_dict"]["wxuin"],
            }
        }
        r1 = requests.post(
            url=url,        #将构造好的信息数据发送给https://wx.qq.com/cgi-bin/mmwebwx-bin/.../pass_ticket={0}
            json = form_data
        )
        r1.encoding = "utf-8"
        user_info = json.loads(r1.text)
        print("user_info:",user_info)
        req.session["current_user"] = user_info["User"] #当前用户所有数据
        for user in user_info["ContactList"]:
            print("最近联系人：",user["NickName"])
        for msg in user_info["MPSubscribeMsgList"]:
            print("最近订阅号信息：", msg)
    return render(req,"index.html",{"user_info":user_info})

def contact_all(req):
    ctime = time.time()
    '''
    对下面地址发送请求获取所有用户列表
    https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxgetcontact?lang=zh_CN&pass_ticket={0}&r={1}&seq=0&skey={2}
    :param req:
    :return:
    '''
    base_url = "https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxgetcontact?lang=zh_CN&pass_ticket={0}&r={1}&seq=0&skey={2}"
    url = base_url.format(req.session["ticket_dict"]["pass_ticket"],ctime,req.session["ticket_dict"]["skey"])
    r1 = requests.get(
        url=url,
        cookies = req.session["ticket_cookie"]      #取用户列表时必须要带ticket_cookie
    )
    r1.encoding = "utf-8"
    contact_dict = json.loads(r1.text)
    return render(req,"contact.html",{"contact_dict":contact_dict})
#收消息
#https://webpush.wx.qq.com/cgi-bin/mmwebwx-bin/synccheck?r=1537781682002&skey=%40crypt_6913cbbc_59ab7e1e83f4d843e0c0dd2957e650b2&sid=5KPGzIltsnHpUvn0&uin=843577301&deviceid=e806266458208600&synckey=1_675357946%7C2_675358122%7C3_675358116%7C11_675357810%7C201_1537781632%7C1000_1537775402%7C1001_1537775474&_=1537776737959
#发消息
#https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxsendmsg?lang=zh_CN&pass_ticket={0}
def send_msg(req):
    ctime = time.time()
    touser = req.GET.get("touser")      #获取 接收者
    msg = req.GET.get("msg")          #获取 发送内容
    base_url = "https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxsendmsg?lang=zh_CN&pass_ticket={0}"
    url = base_url.format(req.session["ticket_dict"]["pass_ticket"])
    form_data = {
        "BaseRequest":{
            "DeviceID": "e513114061127752",
            "Sid":req.session["ticket_dict"]["wxsid"],
            "Skey":req.session["ticket_dict"]["skey"],
            "Uid": req.session["ticket_dict"]["wxuin"],
        },
        "Msg":{
            "ClientMsgId":ctime,
            "Content":msg,
            "FromUserName":req.session["current_user"]["UserName"],
            "LocalID":ctime,
            "ToUserName": touser,
            "type":1
        },
        "Scene":0
    }
    r1 = requests.post(
        url = url,
        data= bytes(json.dumps(form_data,ensure_ascii=False),encoding="utf-8"), #微信内部会自动将data json.dumps
        headers = {"Content-Type":"application/json"},  #自定义请求头为json
    )
    r1.encoding="utf-8"
    print(r1.text)
    return HttpResponse("....")