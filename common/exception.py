"""
@File    :  exception.py
@Time    :  2023/3/17 00:36
@Author  :  luzhenfang
@Version :  1.0
@Desc    :  异常类


1318659507@qq.com
"""
from common.errors import Error


class SysException(Exception):
    def __init__(self, err: Error):
        self.err = err

    def __str__(self):
        return self.err.msg
