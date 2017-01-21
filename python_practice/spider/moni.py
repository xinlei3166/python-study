#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'junxi'

import urllib.request
import urllib.parse
import http.cookiejar


posturl = 'https://www.zhihu.com/login/phone_num'
headers = { 
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
'AppleWebKit/537.36 (KHTML, like Gecko) '
'Chrome/52.0.2743.116 Safari/537.36',
'Referer': 'https://www.zhihu.com/'
}

'''
phone_num ---> 登录名
password ---> 密码
captcha_type ---> 验证码类型
rember_me ---> 记住密码
_xsrf ---> 一个隐藏的表单元素, 防止跨站请求伪造攻击(csrf)
'''

#定义初始登录数据
value = { 
'password':'*****************',
'remember_me':True,
'phone_num':'*******************',
'_xsrf':'**********************'
}

data = urllib.parse.urlencode(value)

#初始化一个cookieJar来处理cookie
cookieJar = http.cookiejar.CookieJar()
cookie_support = urllib.request.HTTPCookieProcessor(cookieJar)

#实例化一个全局opener
opener = urllib.request.build_opener(cookie_support)
request = urllib.request.Request(posturl,data,headers)
result = opener.open(request)
print(result.read())
