# -*- coding:utf-8 -*-

# Author: ChenTong
# Date: 2021/7/14 14:10

from pydantic import BaseModel
from fastapi import Body


class UserAuth(BaseModel):

    # 声明时使用 ... 将其标记为必需参数
    username: str = Body(..., min_length=5, max_length=20, title="用户名")
    password: str = Body(..., min_length=5, max_length=20, title="密码")
