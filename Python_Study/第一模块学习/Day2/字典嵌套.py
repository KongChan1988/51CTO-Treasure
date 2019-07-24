# -*- coding:utf-8 -*-
# Author:D.Gray

av_catalog = {
    '欧美':{
        'www.youporn.com':['很多免费的，世界最大的','质量一般'],
        'www.pornhub.com':['很多免费的，也很大','质量比youporn高点'],
        'letmedothistoyou.com':['多是自拍，高质量图片很多','资源不多,更新慢'],
        'x-art.com':['质量很高，真的很高','全部收费，屌丝请绕过'],
    },
    '日韩':{
        'tokyo-hot':['质量怎样不清楚，个人已经不喜欢日韩范了','听说是免费的'],
    },
    '大陆':{
      '1024':['全部免费，真好，好人一生平安','服务器在国外,慢']
    },
}
av_catalog['大陆']['1024'][1] = '可以在国内做镜像'
print(av_catalog)

print('\n********  .setdefault()方法  *********')
av_catalog.setdefault('taiwan',{'www.baidu.com':[1,2]})  #  .setdefault（）方法  是先去字典中去取相应的 'taiwan'
                                                        #如果取到就不做修改，如果取不到就新增一个，并赋值 'www.baidu.com'
print(av_catalog)

# av_catalog.setdefault('大陆',{'www.baidu.com':[1,2]})  #将上一串代码中的'taiwan'改成'大陆'，取字典中’大陆‘这个值
# print(av_catalog)                                      #字典中包含'大陆'，所以就 不发生改变