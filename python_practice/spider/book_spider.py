#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'junxi'

import urllib.request
import http.cookiejar
import re
import time
import urllib.parse


# 写爬虫不是先写代码，而是先分析网站
'''
爬虫
VIP 一个问题
收费内容
权限, 账号, 登录

第一步:
登录请求 url: http://www.ks5u.com/user/inc/UserLogin_Index.asp
登录请求数据: username=666666&password=666666&c_add=1
请求方式: POST
登录成功之后 cookies身份认证
NO cookie身份证
ajax 异步加载
第二步: 获取内容列表
[]: list 列表 元组
第三步: 获取下载链接
http://www.ks5u.com/USER/INC/Downsch.asp?id=1890066
'''


# 创建一个 cookie对象来保存 cookie
cookie = http.cookiejar.CookieJar()
# 创建一个 cookie对象
handler = urllib.request.HTTPCookieProcessor(cookie)
# 构建一个 handler对象
opener = urllib.request.build_opener(handler, urllib.request.HTTPHandler)
urllib.request.install_opener(opener)
# opener可以直接打开网站

username = '666666'
password = '666666'
params = {
          'username': '666666',
          'password': '666666',
          'c_add': '1',
}

headers = {
'Accept': '*/*',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
'Connection': 'keep-alive',
'Content-Length': '49',
'Content-type': 'application/x-www-form-urlencoded',
'Host': 'www.ks5u.com',
'Origin:http': '//www.ks5u.com',
'Referer': 'http://www.ks5u.com/',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
}

# url = 'http://www.ks5u.com/'
url = "http://www.ks5u.com/user/inc/UserLogin_Index.asp"
# url1 = 'http://www.ks5u.com/user/inc/Login_Index.asp'
data = urllib.parse.urlencode(params).encode()



def login():
    req = urllib.request.Request(url=url, data=data)
    # html = urllib.request.urlopen(url='http://www.ks5u.com/user/inc/UserLogin_Index.asp', data='username=666666&password=666666&c_add=1').read()
    html = opener.open(req).read().decode('gbk')
    return html
    # print(html)



if '666666' in login():
    print('登录成功')
else:
    print('登录失败')


def get_list():
    data_dic = {
        'xueke': '1',
        'shenfen': '32',
    }
    data = urllib.parse.urlencode(data_dic).encode()
    req = urllib.request.Request('http://www.ks5u.com/zhuantimoni/ashx/jinbang.ashx',data=data)
    # req.data('xueke=1&shenfen=32')
    html = opener.open(req).read()
    html = str(html, 'utf-8')   # 解决中文乱码问题
    reg = r'<a href="(.+?)" target="_blank" title="(.+?)">'
    return re.findall(reg, html)        # findall 是进行匹配
    # print(html)


def get_file(id, name):
    req = urllib.request.Request('http://www.ks5u.com/USER/INC/DownCom.asp?id=%s' % id)
    req.add_header('Referer', 'http://www.ks5u.com/zhuantimoni/yimo.html')
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')
    data = opener.open(req).read()
    print(data.decode('gbk'))
    open(name + '.doc', 'wb').write(data)


# get_file('2082674', '辽宁省抚顺市2016届高三第一次模拟考试（3月）语文试题 Word版含答案')

for i in get_list():
    # i = ('1.html', '名字')
    # i[1] = '1.html'
    # i[2] = '名字'
    url = i[0]
    name = i[1]
    id = url.split('/')[-1].split('.')[0]
    # id = url.split('/')[-1][:-6]
    print(id, name)


# req = urllib.request.Request('http://imgsrc.baidu.com/baike/pic/item/91ef76c6a7efce1b1e78f841aa51f3deb58f65ed.jpg')
# data = opener.open(req).read()
# print(data)
# open('aaa' + '.jpg', 'wb').write(data)