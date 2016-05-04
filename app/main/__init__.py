# -*- coding: utf-8 -*-
from flask import Blueprint

#参数为蓝本的名字和蓝本所在的包和模块
main = Blueprint('main',__name__)

#最后导入view,errors，避免循环导入依赖
from . import views, errors