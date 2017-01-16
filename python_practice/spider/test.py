#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'junxi'

from bs4 import BeautifulSoup
import requests


novelurl = 'http://www.23us.com/book/64404'

wb_data = requests.get(novelurl)

# 下面两步解决乱码问题
print(wb_data.encoding, wb_data.apparent_encoding)
wb_data.encoding = wb_data.apparent_encoding

soup = BeautifulSoup(wb_data.text, 'lxml')
# chapterurl = soup.find('a', class_='read').get('href')

info = soup.find('table').text
test = soup.find('table').text.split()[-2]
author = soup.find('table').text.split()[2]

# 作者
# author = soup.find('table').text.split()[2]
# # 更新状态
# status = info.split()[3]
# # 字数
# number = info.split()[6]
# # 类别
# category = info.split[2]
print(info, test, author)
# print(author, status, number)