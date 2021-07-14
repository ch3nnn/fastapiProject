# -*- coding:utf-8 -*-

# Author: ChenTong
# Date: 2021/7/8 13:35

from datetime import datetime

from passlib.context import CryptContext
from sqlalchemy import Column, DateTime, Integer, String, func
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    __table_args__ = {'comment': '用户表'}

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(255), unique=True, nullable=False, comment="用户名")
    password = Column(String(255), unique=True, nullable=False, comment="密码")

    create_time = Column(DateTime, default=datetime.now, server_default=func.now(), comment="创建时间")
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now, server_default=func.now(),
                         server_onupdate=func.now(), comment="更新时间")

    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @classmethod
    def verify_password(cls, plain_password: str, hashed_password: str) -> bool:
        return cls.pwd_context.verify(plain_password, hashed_password)

    @classmethod
    def get_password_hash(cls, password: str) -> str:
        return cls.pwd_context.hash(password)

    @property
    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}

    def __str__(self):
        return self.username
