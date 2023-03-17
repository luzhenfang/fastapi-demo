"""
@File    :  user_repository.py
@Time    :  2023/3/16 22:42
@Author  :  luzhenfang
@Version :  1.0
@Desc    :  用户数据访问层


1318659507@qq.com
"""
from typing import List

from application.core.datasource import MockMongo
from application.models.user import User
from common.decorator import singleton


@singleton
class UserRepository:
    """
     数据访问层  SQL/bson 这里写
    """
    client: MockMongo = MockMongo()

    def add_user(self, user: User):
        self.client.save(user)

    def get_all(self) -> List[User]:
        return self.client.get_all()

    def update_user_byid(self, idx, u: User):
        self.client.update_byid(idx, u)

    def delete_user(self, idx):
        self.client.delete_byid(idx)
