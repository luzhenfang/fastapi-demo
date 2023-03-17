"""
@File    :  middleware.py
@Time    :  2023/3/16 23:26
@Author  :  luzhenfang
@Version :  1.0
@Desc    :  中间件相关


1318659507@qq.com
"""

import abc
from typing import List

from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware


class AbstractMiddleWare(abc.ABC):
    desc: str
    author: str

    @abc.abstractmethod
    async def __call__(self, req: Request, call_next):
        pass


class MiddleWare(AbstractMiddleWare):
    desc = "这是一个默认的中间件"
    author = "luzhenfang"

    async def __call__(self, req: Request, call_next):
        resp = await call_next
        return resp


class ApiMiddleWare:
    _app: FastAPI
    _middleware_lst: List[AbstractMiddleWare] = []

    def __init__(self, a: FastAPI):
        self._app = a

    def use(self, m: AbstractMiddleWare):
        self._middleware_lst.append(m)
        return self

    def _add_middleware(self, m: AbstractMiddleWare):
        info = "😁 (M):{:<30} mounted. {} @{}".format(m.__class__.__name__,m.desc,m.author)
        print(info)

        self._app.add_middleware(BaseHTTPMiddleware, dispatch=m)

    def create(self):
        [self._add_middleware(m) for m in self._middleware_lst]
