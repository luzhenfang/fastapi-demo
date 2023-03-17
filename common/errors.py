"""
@File    :  errors.py
@Time    :  2023/3/17 00:29
@Author  :  luzhenfang
@Version :  1.0
@Desc    :  自定义错误


1318659507@qq.com
"""
from pydantic import BaseModel


class Error(BaseModel):
    code: int
    msg: str


AgeIsNotLegalError = Error(code=3000, msg="用户年龄不合法")


