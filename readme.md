## 项目说明
知识评测工程项目，模板
## 目录结构
- application `应用目录` 
  - core `核心配置目录`
  - models `接口模型定义`
  - routers `路由层`
  - service `应用服务层`
  - repository `数据访问层`
- common `公共组件目录`
- build `构建目录`
- scripts `脚本文件目录`
- tests `单元/集成 测试`


> 按需添加，dto vo 等

## 编码规范
接口统一采用 `RestAPI` 风格。

描述如下:
- `GET` /api/v1/users  获取所有用户
- `POST`/api/v1/users  添加一个用户
- `PUT` /api/v1/users/{uid} 修改指定用户id信息
- `DELETE` /api/v1/users/{uid} 删除 指定id用户

## QA

- Q: 为什么要定义 service 、repository 这些 会不会显得有些麻烦？
- A: 三层架构是经过历史沉淀而得出的一套解决方案。可以满足 `单一职责`，`开闭原则` 等涉及约定。调用链如下 

```text
用户发起请求 -> routers -> service -> repository 
routers: `接口控制层` 用来控制一些请求信息
service: `业务逻辑侧` 这层中主要处理一些业务方法
repository: `数据访问层` 这层中主要编写访问数据库相关逻辑
```

> 建议: 不要将 业务逻辑 放到 数据访问层中。 根据 `单一职责` 限制我们应尽可能的将自己的代码去解耦。


- Q: @singleton 这是一个什么？
- A: 一个装饰器，用来使用单例模式

- Q: 我该如何定义一个中间件?
- A: 参考 `application/core/middleware/error_handler.py` 错误处理 中间件
