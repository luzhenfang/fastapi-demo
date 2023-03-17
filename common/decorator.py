"""
@File    :  decorator.py
@Time    :  2023/3/16 21:24
@Author  :  luzhenfang
@Version :  1.0
@Desc    :  单例模式的装饰器实现


1318659507@qq.com
"""


_ins_map = {}


def singleton(cls):
    global _ins_map

    def get_instance(*args, **kwargs):
        ins = cls(*args, **kwargs)
        if cls not in _ins_map:
            _ins_map[cls] = ins
            return ins
        return _ins_map[cls]

    return get_instance


