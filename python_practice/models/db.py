#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'junxi'

import logging
logging.basicConfig(level=logging.INFO)

import aiomysql
import aioredis
from config.settings import DATABASES, CACHES


def log(sql, args=()):
    logging.info('SQL: %s' % sql, *args)


async def create_pool(loop, **kw):
    """定义mysql全局连接池"""
    logging.info('create database connection pool...')
    global _mysql_pool
    _mysql_pool = await aiomysql.create_pool(host=DATABASES['host'], port=DATABASES['port'], user=DATABASES['user'],
                                      password=DATABASES['password'], db=DATABASES['db'], loop=loop,
                                      charset=kw.get('charset', 'utf8'), autocommit=kw.get('autocommit', True),
                                      maxsize=kw.get('maxsize', 10), minsize=kw.get('minsize', 1))
    return _mysql_pool


async def fetchone(sql, args=(), size=None):
    """封装select，查询单个，返回数据为字典"""
    log(sql, args)
    async with _mysql_pool.acquire() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cur:
            await cur.execute(sql, args)
            rs = await cur.fetchone()
            return rs


async def select(sql, args=(), size=None):
    """封装select，查询多个，返回数据为列表"""
    log(sql, args)
    async with _mysql_pool.acquire() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cur:
            await cur.execute(sql, args)
            if size:
                rs = await cur.fetchmany(size)
            else:
                rs = await cur.fetchall()
            logging.info('rows returned: %s' % len(rs))
            return rs


async def execute(sql, args=()):
    """封装insert, delete, update"""
    log(sql, args)
    async with _mysql_pool.acquire() as conn:
        async with conn.cursor() as cur:
            try:
                await cur.execute(sql, args)
            except BaseException:
                await conn.rollback()
                return
            else:
                affected = cur.rowcount
                return affected


async def create_redis_pool(loop):
    """定义redis全局连接池"""
    logging.info('create redis connection pool...')
    global _reids_pool
    _reids_pool = await aioredis.create_pool(address=CACHES['address'], db=CACHES['db'], password=CACHES['password'],
                                      minsize=CACHES['minsize'], maxsize=CACHES['maxsize'], loop=loop)

    return _reids_pool


async def cache_set(*args, **kwargs):
    """redis set 命令封装"""
    with await aioredis.commands.Redis(_reids_pool) as redis:
        await redis.set(*args, **kwargs)


async def cache_get(*args, **kwargs):
    """redis get 命令封装"""
    with await aioredis.commands.Redis(_reids_pool) as redis:
        return await redis.get(*args, **kwargs)


async def cache_del(*args, **kwargs):
    """redis del 命令封装"""
    with await aioredis.commands.Redis(_reids_pool) as redis:
        return await redis.delete(*args, **kwargs)
