#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'junxi'

import asyncio
import argparse
import uvloop
import aiohttp_debugtoolbar
from aiohttp_debugtoolbar import toolbar_middleware_factory
from aiohttp import web
from application.routes import setup_routes, setup_static_routes, setup_template_routes, setup_session
from models import create_pool, create_redis_pool


async def init(loop):
    mysql_pool = await create_pool(loop)
    redis_pool = await create_redis_pool(loop)
    # app = web.Application(loop=loop, middlewares=[toolbar_middleware_factory])
    # aiohttp_debugtoolbar.setup(app)

    async def dispose_mysql_pool():
        mysql_pool.close()
        await mysql_pool.wait_closed()

    async def dispose_redis_pool():
        redis_pool.close()
        await redis_pool.wait_closed()

    async def dispose_pool(app):
        await dispose_mysql_pool()
        await dispose_redis_pool()

    app = web.Application(loop=loop)
    setup_session(app, redis_pool)
    setup_routes(app)
    setup_static_routes(app)
    setup_template_routes(app)
    app.on_cleanup.append(dispose_pool)
    return app


def main():
    parser = argparse.ArgumentParser(description="aiohttp server start")
    parser.add_argument('--host', type=str, default='127.0.0.1', help='this is a host')
    parser.add_argument('--port', type=str, default='9000', help='this is a port')
    args = parser.parse_args()
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    loop = asyncio.get_event_loop()
    app = init(loop)
    web.run_app(app, host=args.host, port=args.port)


if __name__ == '__main__':
    main()

