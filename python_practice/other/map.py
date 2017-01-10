#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'junxi'


import matplotlib.pyplot as plt

'''matplotlib 绘图'''

# 文字 财务报表
# labels = '一季度', '二季度', '三季度', '四季度'
labels = 'one', 'two', 'three', 'four'
sizes = [20, 30, 25, 25]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
explode = (0, 0, 0, 0)

plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)

plt.axis('equal')

plt.savefig('C://Users/xiaoxinsoso/Pictures/python/pie1.png')
plt.show()

