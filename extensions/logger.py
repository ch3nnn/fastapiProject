# -*- coding:utf-8 -*-

# Author: ChenTong
# Date: 2021/7/14 17:15

# 日志文件,作用:用来记录程序的运行过程,比如:调试信息,接口访问信息,异常信息

import os
import time
from loguru import logger

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

log_path = os.path.join(BASEDIR, 'logs')

if not os.path.exists(log_path):
    os.mkdir(log_path)

log_path_error = os.path.join(log_path, f'{time.strftime("%Y-%m-%d")}_error.log')

# 日志简单配置
logger.add(log_path_error, rotation="12:00", retention="5 days", enqueue=True)


