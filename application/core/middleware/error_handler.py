"""
@File    :  error_handler.py
@Time    :  2023/3/16 23:50
@Author  :  luzhenfang
@Version :  1.0
@Desc    :  错误处理中间件


1318659507@qq.com
"""
from application.core.middleware.middleware import MiddleWare
from common.errors import Error
from common.exception import SysException
from common.response import Response as RestResponse

from fastapi import Request, Response


class ErrorHandler(MiddleWare):
    desc = "异常捕获中间件"
    author = "luzhenfang"

    async def __call__(self, req: Request, call_next):
        try:
            resp = await call_next(req)
            return resp
        except Exception as e:
            # 投递 MQ  接  报警平台
            # xxxxxxxxxxxxxxxxx
            return Response(content=RestResponse.error(Error(code=500, msg=f"{e}")).json())

