from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

"""
    配置数据库连接参数
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://db_username:dbpassword@127.0.0.1/db_name'
    多个数据库支持
        app.config['SQLALCHEMY_BINDS'] = {
            'db1': 'mysql://root:123456@127.0.0.1/flask_orm',
            'db2': 'sqlite://db_path/flask_orm.db'
        }
"""
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:cptbtptp@127.0.0.1/flask_orm'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    """
        ORM 模型字段类型支持
            Integer/Float   整数/浮点类型
            String(size)    有长度限制的字符串
            Text            一些较长的文本（如：文章详情、商品详情）
            DateTime        表示为 Python datetime 对象的时间和日期
            Boolean         存储布尔值
            PickleType      存储为一个持久化的 Python 对象
            LargeBinary     存储一个任意大的二进制数据
    """
    __tablename__ = 'weibo_user'  # 指定表名
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(256), nullable=False)
    birthday = db.Column(db.Date, nullable=True)
    age = db.Column(db.Integer, default=0, comment='生日')


class UserAddress(db.Model):
    """ 用户地址 """
    __tablename__ = 'weibo_user_address'
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(256), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('weibo_user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('address', lazy=True))  # 反向引用（映射 user 和 user address 的对应关系）


"""
    通过反向引用映射了 user 和 user address 的对应关系后，就可以通过以下的方式获取对应的 user 或者 user address
    user = User()
    user.address
    
    address = UserAddress()
    address.user
"""

"""
    新增/修改数据
        构造 ORM 模型对象
            user = User('admin', 'admin@example.com')
        添加到 db.session （备注：可以添加多个对象）
            db.session.add(user)
        提交到数据库
            db.session.commit()
            
    物理删除数据
        查询 ORM 模型对象
            user = User.query.filter_by(username='David').first()
        添加到 db.session
            db.session.delete(user)
        提交到数据库
            de.session.commit()
        
    ORM 查询
        返回结果集（list）
            查询所有结果
                User.query.all()
            按照条件查询
                User.query.filter_by(username='David')
                User.query.filter(User.nickname.endswith('三').all())
            排序
                User.query.order_by(User.username)
            查询 TOP10
                User.query.limit(10).all()
        返回单个 ORM 对象
            根据主键查询
                User.query.get(1)
            获取第一条记录
                User.query.first()
            视图快捷函数，有则返回，没有则返回 404
                first() vs first_or_404()
                get() vs get_or_404()
        多表关联查询
            db.session.query(User).join(Address)
            User.query.join(Address)
            
    分页
        使用 offset 和 limit
            .offset(offset).limit(limit)
        paginate 分页支持
            .paginate(page=2, per_page=10)
            返回 Paginate 对象
                has_prev/has_next   是否有上一页/下一页
                items               当前页的数据列表
                prev_num/next_num   上一页/下一页的页码
                total               总记录数
                pages               总页数
    
    结合模板实现分页
        准备数据
            users = User.query.filter_by(is_valid=1)
        分页
            users.paginate(page=2, per_page=10)
"""


@app.route('/')
@app.route('/index')
def index():
    return 'index'


@app.route('/users/<int:page>')
def users(page):
    """ 用户列表分页 """
    per_page = 10
    user_list = User.query
    user_page_data = user_list.paginate(page=page, per_page=per_page)
    return render_template('users.html', user_page_data=user_page_data)
