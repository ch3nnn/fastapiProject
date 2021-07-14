# -*- coding:utf-8 -*-

# Author: ChenTong
# Date: 2021/7/14 14:44
import traceback

from fastapi_sqlalchemy import db

from extensions import logger
from .models import User


class CRUDUser:

    @classmethod
    def create_user(cls, *, username: str, password: str) -> User:
        user = User(
            username=username,
            password=User.get_password_hash(password)
        )
        try:
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            logger.error(f"{e} -> {traceback.format_exc()}")
            db.session.rollback()
            return None
        return user

    @classmethod
    def authenticate(cls, *, username: str, password: str) -> User:
        if user := db.session.query(User).filter(User.username == username).first():
            if User.verify_password(password, user.password):
                return user
            return None
        return None
