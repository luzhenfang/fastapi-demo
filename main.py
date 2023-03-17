"""
@File    :  main.py
@Time    :  2023/3/16 21:25
@Author  :  luzhenfang
@Version :  1.0
@Desc    :  xxxxx


1318659507@qq.com
"""

from fastapi import FastAPI

import application.core.config.server
from application import routers
from application.core import config
from application.core.middleware.error_handler import ErrorHandler
from application.core.middleware.middleware import ApiMiddleWare
from application.core.middleware.process_time_handler import ProcessTimeHandler

print(config.server.APP_BANNER)

app = FastAPI()
# 注册路由
routers.register(app)

# 注册中间件
ApiMiddleWare(app).use(ErrorHandler()).use(ProcessTimeHandler()).create()


@app.get("/")
def index():
    return {"Hello": "World!"}
