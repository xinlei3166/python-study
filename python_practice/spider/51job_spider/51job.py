#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'junxi'


import urllib.request
import re
import sys


# reload(sys)   # python 2需要设置这个, python 3不需要
# sys.setdefaultencoding('utf-8')  # 输入内容为 utf-8编码




def get_content(page_num):
    url = 'http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=000000%2C00&district=000000&funtype=0000&industrytype=00&issuedate=9&providesalary=99&keyword=python&keywordtype=2&curr_page={}&lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&list_type=0&fromType=14&dibiaoid=0&confirmdate=9'.format(page_num)
    a = urllib.request.urlopen(url)     # 打开网页
    html = a.read()
    html = html.decode('gbk')
    # print(html)
    return html

# get_content('3')


def get(html):
    # (.*?)是取出来, .*?是匹配到但是不取出来
    reg = re.compile(r'class="t1 ">.*?<a target="_blank" title="(.*?)".*?<span class="t2"><a target="_blank" title="(.*?)".*?<span class="t3">(.*?)</span>.*?<span class="t4">(.*?)</span>.*?<span class="t5">(.*?)</span>',re.S)
    items = re.findall(reg, html)
    # print(items)
    return items


# a = get_content('3')
# get(a)


for single_num in range(1, 10):
    html_content = get_content(single_num)

    for i in get(html_content):
        print(i[0], i[1], i[2], i[3])
        with open('51job_python.txt',  'a') as f:      # a 追加模式, 创建新文件
            f.write(i[0] + '\t' + i[1] + '\t' + i[2] + '\t' + i[3] + '\n\n')
            f.close()



