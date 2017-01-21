#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'junxi'

import requests
import urllib.request

url = 'http://mm.263.com/wm2e/mail/login/show/loginShowAction_loginShow.do?usr=itil@yasn.com.cn&sid=Mmk4dDRpOWw2QDJ5NGEwczZu&isp_domain=&useCDN=0&ssl=false'
down_url = 'http://mm.263.com/wm2e/mail/mailOperate/mailOperateAction_mailSaveToStream.do'
# down_url = 'http://imgsrc.baidu.com/baike/pic/item/eaf81a4c510fd9f9503fa2a0202dd42a2934a4cb.jpg'
path = "C://Users/xiaoxinsoso/Documents/收件箱/siwa.png"
'''headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
    'Cookie': 'JSESSIONID=24976FFEBEC9397CD5ACE132C5C6145F.2e112; route=989bc7fe58cb2f9427698ef71e779829; wm_custom_login_username=wangjunjie%40yasn.com.cn; wm_custom_login_wm_ssl=0; route=5423c3a33008db902ce859b639db1ff4; cid_junjie.wang_yasn.com.cn=Tldvd2RURnVNV281YVRWbE9DNDRkelZo; addressSortVal=asecName; cid_itil_yasn.com.cn=TW1rNGREUnBPV3cyUURKNU5HRXdjelp1',
}'''
# 下载文件方法一
r = requests.get(down_url)
with open("C://Users/xiaoxinsoso/Documents/收件箱/siwa.eml", "wb") as file:
    file.write(r.content)
print('OK')

# # 下载文件方法二
# urllib.request.urlretrieve(down_url, path)
# print('Done')


