"""
@File    :  user_service.py
@Time    :  2023/3/16 22:37
@Author  :  luzhenfang
@Version :  1.0
@Desc    :  用户业务逻辑层


1318659507@qq.com
"""
from typing import List

from application.models.user import User
from application.repository.user_repository import UserRepository
from common.decorator import singleton
from common.errors import AgeIsNotLegalError
from common.exception import SysException


@singleton
class UserService:
    """
        业务逻辑这里写，比如说判断请求数据是否合法。 eg: age<=0
    """
    user_repository: UserRepository = UserRepository()

    def add_user(self, user: User):
        if user.age <= 0:
            raise SysException(AgeIsNotLegalError)
        self.user_repository.add_user(user)

    def get_all(self) -> List[User]:
        return self.user_repository.get_all()

    def update_user(self, idx: int, u: User):
        return self.user_repository.update_user_byid(idx, u)

    def delete_user(self, idx: int):
        return self.user_repository.delete_user(idx)
