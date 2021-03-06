# -*- coding:utf-8 -*-

# Author: ChenTong
# Date: 2021/7/8 09:45
from functools import lru_cache

from pydantic import BaseSettings

import logging
import os


# 基本配置信息
class Config(BaseSettings):
    DEBUG = True

    SECRET_KEY = os.getenv('SECRET_KEY', 'dev key')

    BASEDIR = os.path.dirname(os.path.abspath(__file__))

    # 数据库配置
    MYSQL_HOST = os.environ.get('FAST_API_MYSQL_HOST') or "localhost"
    MYSQL_PORT = os.environ.get('FAST_API_MYSQL_PORT') or "3306"
    MYSQL_USER = os.environ.get('FAST_API_MYSQL_USER') or "root"
    MYSQL_PASSWORD = os.environ.get('FAST_API_MYSQL_PASSWORD') or "123456"
    DATABASE = "test"
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{DATABASE}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True  # 数据库内容发送改变之后,自动提交

    # 缓存配置
    CACHE_REDIS_HOST = os.environ.get('FAST_API_REDIS_HOST') or "127.0.0.1"
    CACHE_REDIS_PORT = os.environ.get('FAST_API_REDIS_PORT') or 6379
    CACHE_REDIS_PASSWORD = os.environ.get('FAST_API_REDIS_PASSWORD') or "123456"
    CACHE_REDIS_DB = 0
    CACHE_REDIS_URL = f"redis://:{CACHE_REDIS_PASSWORD}@{CACHE_REDIS_HOST}:{CACHE_REDIS_PORT}/{CACHE_REDIS_DB}?encoding=utf-8"

    # 默认日志等级
    LEVEL = logging.DEBUG

    class Config:
        env_file = ".env"


# 开发模式
class DeveloperConfig(Config):
    pass


# 生产模式
class ProductConfig(Config):
    DEBUG = False
    LEVEL = logging.ERROR


# 测试模式
class TestingConfig(Config):
    pass


# 设置统一访问入口,使用config_dict
config_dict = {
    "develop": DeveloperConfig,
    "product": ProductConfig,
    "testing": TestingConfig
}
