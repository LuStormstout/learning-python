import os.path


class Config(object):
    """ 项目的配置文件 """
    # 数据库连接 URI
    SQLALCHEMY_DATABASE_URI = 'mysql://root:cptbtptp@127.0.0.1/flask_ask_answer_system'
    # 禁用 Flask-SQLAlchemy 事件通知系统
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # flash, from wtf
    SECRET_KEY = 'abcdsacd12312'
    # 文件上传的根路径
    MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'medias')
