from flask import Flask, render_template

app = Flask(__name__, static_folder='assets')


@app.route('/')
def hello_world():
    """ 首页 """
    return render_template('index.html')


@app.route('/follow')
def follow():
    """ 关注 """
    return render_template('follow.html')


@app.route('/login')
def login():
    """ 登录 """
    return render_template('login.html')


@app.route('/register')
def register():
    """ 注册 """
    return render_template('register.html')


@app.route('/write')
def write():
    """ 写文章，提问 """
    return render_template('write.html')


@app.route('/mine')
def mine():
    """ 个人中心 """
    return render_template('mine.html')


@app.route('/detail')
def detail():
    """ 详情页 """
    return render_template('detail.html')
