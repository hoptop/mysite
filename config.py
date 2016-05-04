import os

basedir = os.path.abspath(os.path.dirname(__file__))
#基类配置
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess'
    SQLALCHEMY_COMMIT_ON_TRARDOWN = True
    FLASK_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASK_MAIL_SUBJECT_SENDER = 'Flask Admin<flasky@examplecom>'
    FLASK_ADMIN = os.environ.get('FLASK_ADMIN')
    
    @staticmethod
    def init_app(app):
        pass

#子类配置
class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_PASSWORD')
    SQLLCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlit:///'+ os.path.join(basedir,'data-dev.sqlite')

class TestingConfig(Config):
    TESTING = True
    SQLLCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlit:///'+ os.path.join(basedir,'data-test.sqlite')
       
class ProductionConfig(Config):
     SQLLCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlit:///'+ os.path.join(basedir,'data.sqlite')
        
config = {
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'production':ProductionConfig,
    'default':DevelopmentConfig
}