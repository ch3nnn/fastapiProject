# -*- coding:utf-8 -*-

# Author: ChenTong
# Date: 2021/7/8 10:18
from app.common.result_code import ResultCode
from app.passport import router
from app.passport.schemas import UserAuth
from .curd import CRUDUser
from starlette.requests import Request


@router.post("/register", summary="用户注册")
async def register(*, user_info: UserAuth):
    if CRUDUser.create_user(username=user_info.username, password=user_info.password):
        return ResultCode.success(data=None)
    return ResultCode.error(msg="创建失败")


@router.post("/login", summary="用户登录")
async def login(*, request: Request, user_info: UserAuth):
    """用户登录
    :param request:
    :param user_info:
    :return:
    """
    if user := CRUDUser.authenticate(username=user_info.username, password=user_info.password):
        return ResultCode.success(msg="登录成功", data={"userInfo": user.to_dict})
    return ResultCode.error(msg="用户名或密码错误")


@router.post("/user/logout", summary="用户退出")
def user_logout():
    """用户退出
    """
    return ResultCode.success(data=None)
