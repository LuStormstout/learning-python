import os

from flask import Flask, render_template, redirect, url_for, request
from forms import LoginForm, RegisterForm, UserAvatarForm
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['WTF_CSRF_SECRET_KEY'] = 'YdJkQUe6m5o&98wRB8GxWlpmBbGjuN#$'
app.config['SECRET_KEY'] = '763FQIeix0FZ@jj1y$^RiSZ$iH0lI$wp'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:cptbtptp@127.0.0.1/flask_orm'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 自定义配置扩展，表示文件上传的路径
app.config['UPLOAD_PATH'] = os.path.join(os.path.dirname(__file__), 'medias')
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'weibo_user'  # 指定表名
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(256), nullable=False)
    birthday = db.Column(db.Date, nullable=True)
    age = db.Column(db.Integer, default=0, comment='生日')


"""
    flask-wtf 表单
        集成 wtforms
        CSRF保护
        与 Flask-Uploads 一起支持文件上传
        
    配置 CSRF 保护
        WTF_CSRF_SECRET_KEY = 'a random string'
        
    通过表单保存数据
        检测表单是否已经通过验证
            form.validate_on_submit()
        获取表单中传递过来的值
            form.field_name.data
        业务逻辑代码的编写（集合 ORM）
        
    表单验证
        导入内置的表单验证器（或自定义）
            form.wtforms.validators import DataRequired
        配置到表单字段
            username = StringField(label='用户名', validators=[InputRequired(), my_validators])
            
    内置的表单验证器
        DataRequired/InputRequired  必填项
        Email/URL/UUID              电子邮箱/URL/UUID
        Length(min=-1, max=-1, message=None)    长度范围验证
        EqualTo(field name, message=None)       两个字段输入的值相等（如：密码确认）
    
    自定义表单验证
        场景一：只有本表单使用
        场景二：多个表单中使用
            如：验证手机号码
"""


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/form', methods=['GET', 'POST'])
def page_form():
    """ 表单练习 """
    form = LoginForm()
    if form.validate_on_submit():
        print('登录成功')
    else:
        print(form.errors)
    return render_template('page_form.html', form=form)


@app.route('/user/register', methods=['GET', 'POST'])
def page_register():
    """ 新用户注册 """
    # 用户在提交表单的时候会出发 validate_on_submit
    form = RegisterForm()
    if form.validate_on_submit():
        # 表单验证通过，接下来处理业务逻辑
        # 1、获取表单数据
        username = form.username.data
        password = form.password.data
        birthday = form.birthday.data
        age = form.age.data
        # 2、构建用户对象
        user = User(
            username=username,
            password=password,
            birthday=birthday,
            age=age
        )
        # 3、提交到数据库
        db.session.add(user)
        db.session.commit()
        # 4、跳转到登录页面
        return redirect(url_for('index'))
    else:
        # 打印错误信息
        print(form.errors)
    return render_template('page_register.html', form=form)


@app.route('/image/upload', methods=['GET', 'POST'])
def image_upload():
    """ 不使用 WTF 时实现文件上传 """
    if request.method == 'POST':
        # 获取文件列表
        files = request.files
        file1 = files.get('file1', None)
        if file1:
            # 保存文件
            f_name = secure_filename(file1.filename)
            print(f_name)
            file_name = os.path.join(app.config['UPLOAD_PATH'], f_name)
            file1.save(file_name)
            print('保存成功')
        return redirect(url_for('image_upload'))
    return render_template('image_upload.html')


@app.route('/avatar/upload', methods=['GET', 'POST'])
def avatar_upload():
    """ 头像上传 """
    form = UserAvatarForm()
    if form.validate_on_submit():
        # 获取图片对象
        image = form.avatar.data
        f_name = secure_filename(image.filename)
        file_name = os.path.join(app.config['UPLOAD_PATH'], f_name)
        image.save(file_name)
        print('头像上传成功')
        return redirect(url_for('index'))
    else:
        print(form.errors)
    return render_template('avatar_upload.html', form=form)
