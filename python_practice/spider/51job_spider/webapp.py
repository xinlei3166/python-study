#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'junxi'

import zxxk

urls = ("/", 'Index')
# app = web.application(urls, globals())

class Index:
    def GET(self):
        return render.index()
    def POST(self):
        i = web.input() # 获取用户发起的请求
        url = i.url
        infoid = url.split('/')[-1].split('.')[0]
        link = zxxk.getfile(infoid)
        return link

if __name__ == '__main__':
    web.application(urls, globals()).run()