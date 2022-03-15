from flask import render_template, Blueprint, request

from models import Question

qa = Blueprint('qa', __name__, template_folder='templates', static_folder='../assets')


@qa.route('/')
def index():
    """ 首页 """
    return render_template('index.html')


@qa.route('/follow')
def follow():
    """ 关注 """
    per_page = 20  # 每页的数据量
    page = int(request.args.get('page', 1))
    page_data = Question.query.filter_by(is_valid=True).paginate(page=page, per_page=per_page)
    return render_template('follow.html', page_data=page_data)


@qa.route('/write')
def write():
    """ 写文章，提问 """
    return render_template('write.html')


@qa.route('/detail/<int:q_id>')
def detail(q_id):
    """ 详情页 """
    return render_template('detail.html')
