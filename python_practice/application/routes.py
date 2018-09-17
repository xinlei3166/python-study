#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'junxi'

import aiohttp_jinja2
import jinja2
import uuid
from application.views import Hello, Index, Register, Login, QuestionChoices, Questions, hash_sha256
from config.settings import STATIC_DIR, TEMPLATE_DIR
from aiohttp_session import setup
from aiohttp_session.redis_storage import RedisStorage


def setup_session(app, redis_pool):
    storage = RedisStorage(redis_pool=redis_pool, cookie_name='sessionid', key_factory=lambda: hash_sha256(uuid.uuid4().hex))
    setup(app, storage)


def setup_routes(app):
    app.router.add_view('/hello', Hello, name='Hello')
    app.router.add_view('', Index, name='Index')
    app.router.add_view('/register', Register, name='Register')
    app.router.add_view('/login', Login, name='Login')
    app.router.add_view('/questions/{question_id}/choice', QuestionChoices, name='QuestionChoices')
    app.router.add_view('/questions', Questions, name='Questions')


def setup_static_routes(app):
    app.router.add_static('/static/', path=STATIC_DIR, name='static')


def setup_template_routes(app):
    aiohttp_jinja2.setup(app, filters={'choice_split': choice_split}, loader=jinja2.FileSystemLoader(TEMPLATE_DIR))


def choice_split(choices):
    for i in choices.split(','):
        single = i.split('|')
        yield single

