"""
@File    :  user.py
@Time    :  2023/3/16 22:41
@Author  :  luzhenfang
@Version :  1.0
@Desc    :  用户模型(请求时用)

{
  "name":"jack",
  "age":20
}


1318659507@qq.com
"""
from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int
