"""
@File    :  datasource.py
@Time    :  2023/3/16 22:45
@Author  :  luzhenfang
@Version :  1.0
@Desc    :  模拟操作 mongo  示例代码  很多细节 尚未处理


1318659507@qq.com
"""
from pydantic import BaseModel

from common.decorator import singleton


@singleton
class MockMongo:
    """
        这里只是一个 实例，实际情况要注意处理异常。
        尽管有 异常捕获中间件
    """
    items = []

    def save(self, dto: BaseModel):
        self.items.append(dto)
        print("👉", "MOCK:", "save", dto)

    def update_byid(self, id: int, dto: BaseModel):
        self.items[id] = dto
        print("👉", "MOCK:", "update", dto)

    def get_all(self):
        return self.items

    def delete_byid(self, id: int):
        del self.items[id]
