# coding:utf-8

from flask import Flask, render_template, current_app, g, request, session, make_response, \
    redirect, abort, flash

app = Flask(__name__)
# 为模板引擎添加扩展，支持 break/continue
app.jinja_env.add_extension('jinja2.ext.loopcontrols')
# session secret_key
app.secret_key = 'pA74dpHu58EVkyPx!nyiNRP8w@3J2Dsp'

""" Flask 框架入门 """


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
# @app.route('/user')
# @app.route('/user/<page>')
# def list_user(page=1):
#     return '你好，你是第 {} 页用户'.format(page)


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


""" Flask 模板语法与继承 """


# 模板标签的练习
@app.route('/template/tag')
def template_tag():
    # 1、简单的数据类型的渲染
    age = 23
    money = 65.32
    name = '张三丰'

    # 2、dict 数据类型的渲染
    #   {{ object.attribute }} 或 {{ object['attribute'] }}
    userinfo = {
        'username': '关羽',
        'nickname': '二哥',
        'address.city': '荆州市',
        'address.area': '朝阳区'
    }

    # 3、元组和列表（tuple/list）数据类型的渲染
    tuple_city = ('北京', '上海', '广州', '深圳', '杭州', '成都')
    list_city = ['北京', '上海', '广州', '深圳', '杭州', '成都']

    # 4、list/tuple 嵌套 dict 复杂数据类型的渲染
    user_list = [
        {
            'username': '刘备',
            'address': {
                'city': '成都'
            },
        },
        {
            'username': '曹操',
            'address': {
                'city': '洛阳'
            },
        },
        {
            'username': '孙权',
            'address': {
                'city': '南京'
            },
        },
    ]

    # 模板标签的使用
    var = None
    a = 2
    user_list_loop = [
        {'username': '刘备', 'age': '45', 'address': '成都'},
        {'username': '曹操', 'age': '52'},
        {'username': '张三', 'age': '18', 'address': '北京'},
        {'username': '李四', 'age': '21'}
    ]

    return render_template('template-tag.html', age=age, money=money, name=name, userinfo=userinfo,
                           tuple_city=tuple_city, list_city=list_city, user_list=user_list, var=var, a=a,
                           user_list_loop=user_list_loop)


""" 
    模版语法之过滤器
    过滤器：修改变量（如：格式化显示）
    用管道符号（｜）分割 {{ name|striptags }}
    可以链式调用 {{ name|striptags|title }}
    可以用圆括号传递可选参数 {{ list|join(',') }}
    使用：
        用管道符号（｜）
            {{ value|safe }}
        使用标签
            {% filter upper %}
                This text becomes uppercase
            {% endfilter %}
            
    内置的过滤器
        求绝对值
            {{ value|abs }}
        默认值显示 default(value, default_value='', boolean=False)
            {{ value|default('默认值') }}
            {{ value|d('默认值') }} 简写方式
        HTML 转义
            {{ value|escape }} 或 {{ value|e }}
        富文本内容的转义显示
            {{ value|safe }}
        倒序显示
            {{ value|reverse }}
            
    自定义过滤器
        使用装饰器注册
            @app.template_filter('reverse')
            def reverse_filter(s):
                return s[::-1]
        调用函数注册
            def reverse_filter(s):
                return s[::-1]
            app.jinja_env.filters['reverse'] = reverse_filter
    
"""


@app.route('/template/filter')
def template_filter():
    welcome = 'Hello Lu Stormstout'
    var = None
    html_value = '<h2>这是 H2 标签</h2>'
    phone_number = '12312345678'
    return render_template('template-filter.html', welcome=welcome, var=var, html_value=html_value,
                           phone_number=phone_number)


@app.template_filter('phone_format')
def phone_format(phone_number):
    """ 电话号码脱敏处理过滤器 """
    # 12312345678 -> 123****5678
    return phone_number[0:3] + '****' + phone_number[7:]


@app.route('/template/global-func')
def global_func():
    """ 模板全局函数的使用 """
    return render_template('global_func.html')


""" 
  什么是宏：
    把常用的功能抽出来，可实现重用
    简单理解 宏 约等于 函数
    宏可以写在单独的 HTML 文件中
  模板中的宏
    像写函数一样定义宏
    {% macro input(name, value='', type='text', size=20) -%}
        <input type="{{ type }}" name="{{ name }}" value="{{ value|e }}" size="{{ size }}">
    {%- endmacro %}
    
  文件中的宏
    将前面定义的宏保存为 forms.html
    导入
        {% import 'forms.html' as forms %}
        {% from 'forms.html' import input %}
    使用 <p>{{ forms.input('username') }}</p>
"""


@app.route('/template/macro')
def macro():
    """ 模板中宏的使用 """
    return render_template('macro.html')


"""
    Flask 模板语法与继承
    一、将可变的部分圈出来 (base.html)
        {% block content %}
            <!-- 内容区域 -->
        {% endblock %}
        
    二、继承父模板
        {% extends 'base.html' %}
        
    三、填充新的内容
        {% extends 'base.html' %}
        {% block content %}
            <!-- 新的内容 -->
        {% endblock %}
    四、复用父模板的内容
        {% extends 'base.html' %}
        {% block header %}
            {{ super() }}
            <!-- 新的菜单内容 -->
        {% endblock %}
        
    Flask 模板包含实现
        一、将可变的部分拆出来 (sidebar.html)
            <div>
                这是右侧公共的部分
            </div>
        二、将拆出来的部分包进来 (index.html)
            {% extends 'base.html' %}
            {% block content %}
                <!-- 页面主要内容区域 -->
                
                {# 公用的区域 #}
                {% include 'sidebar.html' %}
            {% endblock %}
            
    Flask 模板中的代码复用
        当前页面的代码复用
            <title>{% block title %}{% endblock %}</title>
            <h1>{{ self.title() }}</h1>
            {% block content %}
            {% endblock %}
            
    相关的模板标签
        {% block sidebar %} {% endblock %}  命名代码块
        {% extends 'base.html' %}           继承模板
        {% include 'header.html' %}         包含代码块
            
"""


@app.route('/extends')
def template_extends_index():
    """  首页 """
    return render_template('extends/index.html')


@app.route('/extends/course')
def course():
    """  免费课程 """
    return render_template('extends/course.html')


@app.route('/extends/coding')
def coding():
    """  实战课程 """
    return render_template('extends/coding.html')


@app.route('/extends/article')
def article():
    """  手记 """
    return render_template('extends/article.html')


@app.route('/extends/wenda')
def wenda():
    """  问答页面 """
    question = 'why?'
    return render_template('extends/wenda.html', question=question)


"""
    消息闪现
        一、在视图中产生一个消息（提示/警告/错误）
            flash(message_content, message_type)
            参数 message_content  消息内容
            参数 message_type     消息类型
        二、在模板中展示消息
            get_flashed_messages(category_filter=['error'])
            参数 category_filter 对产生的消息类型按类别查询
            <ul>
                {% for category, message in get_flashed_messages(with_categories=true) %}
                    <li class="{{ category }}">{{ message }}</li>
                {% endfor %}
            </ul>
"""


#  用户登录之后，跳转到个人中心页面，在个人中心页面，展示一个提示（登录成功）


@app.route('/login', methods=['GET', 'POST'])
def login():
    """ 用户登录 """
    if request.method == 'POST':
        print('处理了登录的逻辑')
        flash('登录成功', 'success')
        flash('欢迎回来', 'success')
        flash('错误提示', 'error')
        return redirect('/mine')
    else:
        return render_template('login.html')


@app.route('/mine')
def mine():
    """ 个人中心 """
    return render_template('mine.html')
