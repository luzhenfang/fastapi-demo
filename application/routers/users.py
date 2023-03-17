"""
@File    :  users.py
@Time    :  2023/3/16 21:50
@Author  :  luzhenfang
@Version :  1.0
@Desc    :  用户相关路由


1318659507@qq.com
"""

from fastapi import APIRouter, Depends
from fastapi.params import Path

from application.core.config.api import ROUTER_PREFIX_V1
from application.models.user import User
from application.service.user_service import UserService
from common.errors import AgeIsNotLegalError
from common.exception import SysException
from common.response import Response

router = APIRouter(prefix=ROUTER_PREFIX_V1, tags=["user"])


# 可以提到 单独一个文件夹中
async def _user_service():
    return UserService()


@router.get("/users", response_model=Response)
async def get_all_user(user_service: UserService = Depends(_user_service)):
    """
    :param user_service:  自动依赖注入
    :return:  返回 统一 Response 类型
    获取全部用户
    """
    users = user_service.get_all()
    return Response.success(users)


@router.post("/users")
async def add_user(user: User, user_service: UserService = Depends(_user_service)):
    """
    新增一个用户
    :param user:
    :param user_service:
    :return:
    """
    user_service.add_user(user)
    return Response.success()


@router.put("/users/{uid}")
async def update_user_by_id(uid: int, user: User, user_service: UserService = Depends(_user_service)):
    """
    更改一个用户(通过ID)
    :param uid:
    :param user:
    :param user_service:
    :return:
    """
    user_service.update_user(uid, user)
    return Response.success()


@router.delete("/users/{uid}")
async def delete_user(uid: int, user_service: UserService = Depends(_user_service)):
    """
    删除一个用户 (通过ID)
    :param uid:
    :param user_service:
    :return:
    """
    user_service.delete_user(uid)
    return Response.success()
