"""
@File    :  response.py
@Time    :  2023/3/16 21:57
@Author  :  luzhenfang
@Version :  1.0
@Desc    :  通用返回类


1318659507@qq.com
"""
from typing import Any, Optional

from pydantic import BaseModel

from common.errors import Error

success_code = 2000


class Response(BaseModel):
    code: int
    msg: str
    data: Optional[Any]

    @staticmethod
    def success(data: Any = None):
        return Response(code=success_code, msg="success", data=data)

    @staticmethod
    def error(err: Error):
        return Response(code=err.code, msg=err.msg, data=None)
