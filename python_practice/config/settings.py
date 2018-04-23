#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'junxi'

import os

DATABASES = {
    'engine': 'mysql',
    'db': 'vote',
    'user': 'vote',
    'password': '123456',
    'host': 'localhost',
    'port': 3306,
}

CACHES = {
    'engine': 'redis',
    'address': ('localhost', 6379),
    'password': None,
    'db': None,
    'minsize': 1,
    'maxsize': 10
}

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))      # 项目路径
STATIC_DIR = os.path.join(BASE_DIR, 'static')       # 静态文件路径
TEMPLATE_DIR = os.path.join(BASE_DIR, 'template')   # 模版HTML路径



