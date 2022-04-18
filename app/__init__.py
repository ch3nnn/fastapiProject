# -*- coding:utf-8 -*-

# Author: ChenTong
# Date: 2021/7/8 09:24


# 权限模块 https://github.com/raddevon/flask-permissions
# from flask_permissions.core import Permissions

from aioredis import create_redis_pool
from fastapi import FastAPI, Request
from fastapi_sqlalchemy import DBSessionMiddleware  # middleware helper
from starlette.responses import JSONResponse

from app import passport, websocket
from config import config_dict


# 工厂方法,根据不同的参数,创建不同环境下的app对象
def create_app(config_name):
    settings = config_dict[config_name]()

    app = FastAPI()

    # 挂载db
    app.add_middleware(DBSessionMiddleware, db_url=settings.SQLALCHEMY_DATABASE_URI)
    # 挂载redis
    register_redis(app, settings)
    # 添加路由
    app.include_router(passport.router, prefix="/api")
    app.include_router(websocket.router)  # websocket

    app.config = settings

    @app.exception_handler(Exception)
    async def all_exception_handler(request: Request, exc: Exception):
        print(f"参数不对{request.method} {request.url}")  # 可以用日志记录请求信息,方便排错
        return JSONResponse({"code": "500", "message": exc})

    return app


def register_redis(app: FastAPI, settings) -> None:
    """
    把redis挂载到app对象上面
    :param settings:
    :param app:
    :return:
    """

    @app.on_event('startup')
    async def startup_event():
        """
        获取链接
        :return:
        """
        app.state.redis = await create_redis_pool(settings.CACHE_REDIS_URL)

    @app.on_event('shutdown')
    async def shutdown_event():
        """
        关闭
        :return:
        """
        app.state.redis.close()
        await app.state.redis.wait_closed()



