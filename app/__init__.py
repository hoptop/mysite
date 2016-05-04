# encoding=utf-8

from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
# from flask.mail import Mail
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLALchemy
from config import config

#创建扩展类，此时传入参数
bootstrap = Bootstrap()
# mail = Mail()
moment = Moment()
db = SQLALchemy()

#工厂函数
def create_app(config_name):
    #实例化
    app = Flask(__name__) 
    #导入配置信息
    app.config.from_object(config[config_name]) 
    #调用init_app()初始化扩展
    config[config_name].init_app(app)   
    bootstrap.init_app(app)
    # mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    
    #附加路由和自定义的错误页面
    from .main import main as main_blueprint #导入蓝本
    app.register_blueprint(main_blueprint)   #注册蓝本
    
    return app