#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'junxi'

import urllib.parse
import urllib.request
import re

cookie = 'xk.tmpl.userstate=state_html%3D%250D%250A%250D%250A%2520%2520%2520%2520%253Cspan%2520class%253D%2522un-login%2522%2520id%253D%2522un-login%2522%253E%250D%250A%2520%2520%2520%2520%2520%2520%2520%2520%253Ca%2520href%253D%2522http%253A%252F%252Fwxt.zxxk.com%2522%2520class%253D%2522bind-btn%2522%253EIP%25E7%25BB%2591%25E5%25AE%259A%25E4%25BC%259A%25E5%2591%2598%25E9%2580%259A%25E9%2581%2593%253C%252Fa%253E%250D%250A%2520%2520%2520%2520%2520%2520%2520%2520%253Ca%2520href%253D%2522https%253A%252F%252Fsso.zxxk.com%252Flogin%253Fservice%253Dhttp%25253A%25252F%25252Fgw.open.zxxk.com%25252Frouter%25253F%252524method%25253Dxk.user.callback%252526%252524app_key%25253Dc4ca4238a0b923820dcc509a6f75849b%252526curl%25253Dhttp%2525253A%2525252F%2525252Fwww.zxxk.com%2525252F%2522%2520class%253D%2522login-btn%2522%253E%25E7%2599%25BB%25E5%25BD%2595%253C%252Fa%253E%250D%250A%2520%2520%2520%2520%2520%2520%2520%2520%253Ca%2520href%253D%2522https%253A%252F%252Fsso.zxxk.com%252Fuser%252Fsignup%253Fservice%253Dhttp%25253A%25252F%25252Fgw.open.zxxk.com%25252Frouter%25253F%252524method%25253Dxk.user.callback%252526%252524app_key%25253Dc4ca4238a0b923820dcc509a6f75849b%252526curl%25253Dhttp%2525253A%2525252F%2525252Fwww.zxxk.com%2525252F%2522%2520class%253D%2522reg-btn%2522%253E%25E6%25B3%25A8%25E5%2586%258C%253C%252Fa%253E%250D%250A%2520%2520%2520%2520%2520%2520%2520%2520%253Cb%253E%257C%253C%252Fb%253E%250D%250A%2520%2520%2520%2520%253C%252Fspan%253E%250D%250A%26type%3D2%26login_state%3Dfalse%26uid%3D; xk.passport=AA223C30E8AABDA70EA4C775B66413E457EF02C5679AD466BD2B76FF7AC5ACCB6E18FEF21D2067FF0025E25DDAD828F05A79C7C3F806EF3145DCAFE9171FE3CF90F9FDE5139B3B8DEAEA40B85C20A40D50E4631044D7FFC4C6A35D7EF778DC25A7E00C37FC02D7F366B0043E1B0C0203D603E6FD77905E274794BE27210C55554A03BCF6D45F8A6217F92EE60FF06A71D3EA092370EFC52003AD6195C42AD3B23C0E543F27C3BF95A86E9B8498E89487FAAA3796AF89F508F4EB0B4809F1773A46471EE9081043EC92FF6B334317F702CCAE4703FFBCD90BD359601C268C0C24F7EBA15E35E4D17EC092DAE4A68987444C82CE1553C722FA19BA1CA41E667CC48825E90DF1960F97576C90256BD42F4B752F3383C0F6CF84AB6A34E592D4C8B68A2C08BC59DD506B6F0F5F7C72C784EEBF3C091346FF6C4146AC5F8B9BA72CCD72FC9A3AEE37F7F97CC279F216FB8A5A3B667A7BE76CC88383BB1AC3C9FBCE64D2190F9BFFBC0388AAA8715DC86DF498E2A6192A93CB7F2C67A51A06DFD0C24002FBF019A0511850D1985715112201FD0F5135D00A9CE7CDC774FD43F7B33FA7CFC44D1C14906BDE66E8D5D9F1DA4B5ED317E5F8B6B10305F554ED04; xk.passport.uid=25469815; ASP.NET_SessionId=if3rn101qpb1pnbz4ch31svu; CNZZDATA1759807=cnzz_eid%3D1835696219-1483964848-%26ntime%3D1483964848; Hm_lvt_0e522924b4bbb2ce3f663e505b2f1f9c=1483967530; Hm_lpvt_0e522924b4bbb2ce3f663e505b2f1f9c=1483967865; cn_1759807_dplus=%7B%22distinct_id%22%3A%20%22159835b83ae39-0cdacbf65d5cca-3e64430f-1fa400-159835b83af59%22%2C%22%24_sessionid%22%3A%200%2C%22%24_sessionTime%22%3A%201483967877%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201483967877%7D'

def get_list():
    # req = urllib.request.urlopen('http://user.zxxk.com')
    # req = urllib.request.Request('http://user.zxxk.com')
    req = urllib.request.Request('http://www.zxxk.com/zj/info/10299')
    req.add_header('cookie', cookie)
    html = urllib.request.urlopen(req)
    # print(req.geturl()) # geturl = 获取地址url
    reg = r'<a href="http://www.zxxk.com/soft/(.*?).html" target="_blank" title="(.*?)">.*?</a>'
    # print(html.read().decode('utf-8')) # geturl = 获取地址url
    return re.findall(reg, html)
    # print(re.findall(reg, html))

# get_list()

def get_file(infoid):
    html = urllib.request.urlopen('http://www.zxxk.com/soft/%s.html')% infoid
    reg = r'<title>(.*?)</title>'
    name = re.findall(reg, html)
    req = urllib.request.Request('http://download.zxxk.com//?UrlID=29&InfoID=%s&') % (infoid)
    req.add_header('cookie', cookie)
    files = urllib.request.urlopen(req).read()  # 文件
    with open('%s.doc' % name.decode('utf-8'), 'wb') as fn:
        fn.write(files)
    return '%s----下载完成' % name

for infoid in get_list(): # [('12345', '这是名字'), ('12345', '名字')]
    print('开始下载')







'''
http://download.zxxk.com//?UrlID=29&InfoID=2670765&key=4e6d0bbf9a17b7380bc164b7e97fa380
http://download.zxxk.com//?UrlID=29&InfoID=2670764&key=be27f64283d2b6d7990daadd27590a0b

'''