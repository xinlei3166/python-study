#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'junxi'


from bs4 import BeautifulSoup
import requests

url = 'http://www.23us.com/class/3_8.html'
headers = {
'Connection': 'keep-alive',
'Cookie': 'targetEncodingwww23uscom=2; CNZZDATA1261058513=901820474-1484700448-%7C1484700448',
'Host': 'www.23us.com',
'Referer': 'http://www.23us.com/',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}

wb_data = requests.get(url=url, headers=headers)
wb_data.encoding = wb_data.apparent_encoding
print wb_data.apparent_encoding
soup = BeautifulSoup(wb_data.text, 'lxml')

for i in soup.select('td.L a'):
    # print i.get('href')
    if i.get('href').split('//')[1].split('/')[1] == 'book':    # 判断是否为小说url和目录，排除章节url
        print i.text
        print i.get('href')






