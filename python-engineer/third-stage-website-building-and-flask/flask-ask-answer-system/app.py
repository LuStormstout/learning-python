from flask import Flask
from models import db

from accounts.views import accounts
from qa.views import qa

app = Flask(__name__, static_folder='assets')

# 从配置文件加载配置
app.config.from_object('conf.Config')

# 数据库初始化
db.init_app(app)

# 注册蓝图
app.register_blueprint(accounts, url_prefix='/accounts')
app.register_blueprint(qa, url_prefix='/')
