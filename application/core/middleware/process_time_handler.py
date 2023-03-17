"""
@File    :  process_time_handler.py
@Time    :  2023/3/16 22:58
@Author  :  luzhenfang
@Version :  1.0
@Desc    :  记录程序处理时间 中间件


1318659507@qq.com
"""
import time

from fastapi import Request

from application.core.middleware.middleware import MiddleWare
from common.decorator import singleton


class ProcessTimeHandler(MiddleWare):
    desc = "记录处理时间中间件"
    author = "luzhenfang"

    async def __call__(self, req: Request, call_next):
        start_time = time.time()
        resp = await call_next(req)
        process_time = time.time() - start_time
        tformat = lambda t: "{:.3f}s".format(t * 100)
        resp.headers["X-Process-Time"] = tformat(process_time)
        return resp
