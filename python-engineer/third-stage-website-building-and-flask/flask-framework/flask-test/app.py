# coding:utf-8

from flask import Flask, render_template, current_app, g, request, session, make_response, \
    redirect, abort

app = Flask(__name__)


@app.route('/index')
def index():
    # print(app)
    # print(current_app)
    # print(app is current_app)
    # print(request)
    return 'index'


@app.route('/')
def hello_world():
    return 'Hello Flask!'


# 传递参数
# @app.route('/userinfo/<username>')
# URL 参数类型
#   string  接受任何不包含斜杠的文本（默认值）
#   int     接受正整数
#   float   接受正浮点数
#   path    类似于 string 但是可以包含斜杠
#   uuid    接受UUID字符串
# 指定参数类型
# @app.route('/post/<int:post_id>')
@app.route('/hello')
def hello():
    user = {
        'name': 'Jacklu'
    }
    return render_template('hello.html', user=user)


# 传递和接收参数以及默认值
@app.route('/user')
@app.route('/user/<page>')
def list_user(page=1):
    return '你好，你是第 {} 页用户'.format(page)


# app.add_url_rule('/home', 'home', hello_world)

# print(app.url_map)

# request 请求报文常用参数
#   method  请求的类型
#   form    POST 请求数据 dict
#   args    GET 请求数据 dict
#   values  POST 请求和 GET 请求数据的集合 dict
#   files   上传的文件数据 dict
#   cookies 请求中的 cookie dict
#   headers HTTP 请求头

# 请求报文练习
@app.route('/test/request')
def test_request():
    get_args = request.args
    print(get_args)
    page = request.args.get('page', 1)
    username = request.args.get('username')
    print(f'page: {page} username: {username}')

    # 获取服务器主机地址
    host = request.headers.get('host')
    print(f'host: {host}')
    # 获取 ip 地址
    ip = request.remote_addr
    print(f'客户端 IP 地址: {ip}')
    user_agent = request.headers.get('user-agent', None)
    print(f'User-Agent: {user_agent}')
    return 'request success'


# 请求钩子
#   before_first_request    服务器启动后第一个请求到达前执行
#   before_request          每一个请求到达前执行
#   after_request           每次请求处理完成之后执行，如果请求过程中产生了异常，则「不执行」
#   teardown_request        每次请求处理完成之后都会执行，如果请求过程中产生了异常也会「正常执行」

# 服务器启动后第一个请求到达前执行
@app.before_first_request
def first_request():
    print('********** FIRST REQUEST **********')


# 每一个请求到达前执行
@app.before_request
def per_request():
    print('********** BEFORE REQUEST **********')


# 响应
#   可以是字符串
#   可以是元组（tuple）
#       (response, status, headers) 或 (response, headers)
#       response    响应内容
#       status      响应状态码
#       headers     响应头信息

@app.route('/test/response')
def test_response():
    # return 'response success', 201, {
    #     'user_id': 12,
    #     'username': 'Jack Lu'
    # }

    # 通过 make_response 构造一个响应对象
    # response = make_response('这是一个响应对象', 401, {
    #     'token': 'abc123456',
    #     'post_id': 652
    # })
    # response.headers['user_id'] = 98
    # response.status_code = 400

    # 响应 HTML
    html = "<html><body><h1 style='color:red'>HTML 文本显示</h1></body></html>"
    response = make_response(html)

    return response


# 从文件中响应 HTML
@app.route('/test/html')
def test_html():
    html = render_template('index.html')
    response = make_response(html, 400)
    return response


# 重定向
# 请求 「/test/redirect」 时重定向到 「/index」 页面
@app.route('/test/redirect')
def test_redirect():
    return redirect('/index')


# abort() 处理错误，不需要 return
@app.route('/test/abort')
def test_abort():
    # ip 拦截场景
    ip_list = ['127.0.0.1']
    ip = request.remote_addr
    if ip in ip_list:
        abort(403)
    return 'hello abort test'


# 错误拦截处理
@app.errorhandler(403)
def forbidden_page(err):
    print(err)
    return '你没有权限访问，请联系管理员。'

# 不推荐的写法
# if __name__ == '__main__':
#     app.run()
