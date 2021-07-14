# -*- coding:utf-8 -*-

# Author: ChenTong
# Date: 2021/7/8 17:26

import datetime
import json
import typing
from typing import Union

from fastapi import status
from fastapi.responses import Response


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return json.JSONEncoder.default(self, obj)


class JSONResponse(Response):
    media_type = "application/json"

    def render(self, content: typing.Any) -> bytes:
        return json.dumps(
            content,
            ensure_ascii=False,
            allow_nan=False,
            indent=None,
            separators=(",", ":"),
            cls=DateEncoder
        ).encode("utf-8")


class ResultCode:

    @classmethod
    def error(cls, *, msg: str = "请求失败"):
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                'code': 0,
                'msg': msg,
                'data': None,
            }
        )

    @classmethod
    def success(cls, *, msg: str = "success", data: Union[list, dict, str] = None) -> Response:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                'code': 1,
                'msg': msg,
                'data': data,
            }
        )
