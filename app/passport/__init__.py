# -*- coding:utf-8 -*-

# Author: ChenTong
# Date: 2021/7/12 10:10

from fastapi import APIRouter

router = APIRouter(prefix="/user")

from .views import *
