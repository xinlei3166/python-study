#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'junxi'

import datetime
import decimal
import hashlib
import re
import aiohttp_jinja2
import json
from aiohttp import web
from models import select, execute, fetchone, cache_set, cache_get, cache_del
from aiohttp_session import get_session
from functools import wraps


class RewriteJsonEncoder(json.JSONEncoder):
    """重写json类，为了解决datetime类型的数据无法被json格式化"""

    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")
        elif isinstance(obj, decimal.Decimal):
            return str(obj)
        elif hasattr(obj, 'isoformat'):
            # 处理日期类型
            return obj.isoformat()
        else:
            return json.JSONEncoder.default(self, obj)


def json_dumps(obj):
    return json.dumps(obj, cls=RewriteJsonEncoder)


def hash_sha256(password):
    """sha256加密"""
    h = hashlib.sha256('vote'.encode('utf-8'))
    h.update(password.encode('utf-8'))
    return h.hexdigest()


def login_required(func):  # 用户登录状态校验
    """This function applies only to class views."""
    @wraps(func)
    async def inner(cls, *args, **kwargs):
        session = await get_session(cls.request)
        uid = session.get("uid")
        if uid:
            user = await fetchone('select id, name, email, phone from user where id = %s', (uid,))
            cls.request.app.userdata = user
            return await func(cls, *args, **kwargs)
        else:
            return web.Response(status=302, headers={'location': '/login'})

    return inner


def api_required(func):  # 接口登录状态校验
    """This function applies only to class views."""
    @wraps(func)
    async def inner(cls, *args, **kwargs):
        session = await get_session(cls.request)
        uid = session.get("uid")
        if uid:
            user = await fetchone('select id, name, email, phone from user where id = %s', (uid,))
            cls.request.app.userdata = user
            return await func(cls, *args, **kwargs)
        else:
            msg = {"status": 1, "msg": "User not logined in"}
            return web.json_response(msg)

    return inner


def permission_check(permission):  # 权限校验
    def outer(func):
        @wraps(func)
        def inner(request, *args, **kwargs):
            user_permission = request.get("userdata").get("user_permission")
            group_permission = request.get("userdata").get("group_permission")
            if permission in user_permission or permission in group_permission:
                return func(request, *args, **kwargs)
            else:
                msg = {"status": 2, "msg": "Permission Denied."}
                return web.json_response(msg)

        return inner

    return outer


class Hello(web.View):
    """a basic web handler example"""

    async def get(self):
        return web.Response(text='Hello Aiohttp!')


class Index(web.View):
    """a view handler for home page"""

    @login_required
    async def get(self):
        # response.headers['Content-Language'] = 'utf-8'
        return aiohttp_jinja2.render_template('index.html', self.request, locals())


class Register(web.View):
    """a view handler for register page"""

    @aiohttp_jinja2.template('register.html')
    async def get(self):
        return

    async def post(self):
        data = await self.request.post()
        user = await fetchone('select id from user where email = %s or phone = %s', (data.get('email'), data.get('phone')))
        # print(await self.request.multipart())
        if user:
            msg = {'error_code': 20001, 'error_msg': 'The email or phone has been registered'}
        else:
            params = (data.get('name'), data.get('email'), data.get('phone'), data.get('password'))
            result = await fetchone('INSERT INTO user(name, email, phone, password) VALUES(%s, %s, %s, %s)', params)
            if result:
                msg = {'error_code': 0, 'error_msg': 'ok'}
            else:
                msg = {'error_code': 20002, 'error_msg': 'Please try again if registration fails'}
        # return web.json_response(data=msg, dumps=json_dumps)
        return web.json_response(data=msg, dumps=json_dumps)


class Login(web.View):
    """a view handler for login page"""

    async def get(self):
        return aiohttp_jinja2.render_template('login.html', self.request, locals())

    async def post(self):
        data = await self.request.post()
        account = data.get('account')
        password = data.get('password')
        columns = 'id, name, email, phone, password'
        if len(account) == 11 and re.match(r'^1[35678]\d{9}', account):
            user = await fetchone('select {} from user where phone = %s'.format(columns), (account,))
        elif re.match(r'^[\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)+$', account):
            user = await fetchone('select {} from user where email = %s'.format(columns), (account,))
        else:
            msg = {'error_code': 20003, 'error_msg': 'User does not exists'}
            return aiohttp_jinja2.render_template('login.html', self.request, locals())
        if password != user.get('password'):
            msg = {'error_code': 20004, 'error_msg': 'Password mismatch'}
            return aiohttp_jinja2.render_template('login.html', self.request, locals())
        session = await get_session(self.request)
        session['uid'] = user.get('id')
        # sessionid = session.identity
        return web.Response(status=302, headers={'location': '/'})


class QuestionChoices(web.View):
    """a view handler for look at the choice to the question"""

    @login_required
    async def get(self):
        question_id = self.request.match_info.get('question_id')
        result = await select('select * from choice where question_id = %s', (question_id,))
        return web.json_response(data=result, dumps=json_dumps)


class Questions(web.View):
    """a view handler for look at all questions"""

    @login_required
    async def get(self):
        questions = await select('select q.id as qid, q.question_text, (select group_concat(concat_ws("|", c.id, c.choice_text)) from choice c where c.question_id = q.id) as question_choice from question q;')
        return aiohttp_jinja2.render_template('questions.html', self.request, locals())

