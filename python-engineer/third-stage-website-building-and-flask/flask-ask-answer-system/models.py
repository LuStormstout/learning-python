from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

from utils import constants

db = SQLAlchemy()


class User(db.Model):
    """ 用户模型 """
    __tablename__ = 'accounts_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), unique=True, nullable=False, comment='用户名')
    nickname = db.Column(db.String(64), comment='昵称')
    password = db.Column(db.String(256), nullable=False, comment='密码')
    avatar = db.Column(db.String(256), comment='头像地址')
    status = db.Column(db.SmallInteger, default=constants.UserStatus.USER_ACTIVE.value, comment='状态')
    is_super = db.Column(db.SmallInteger, default=constants.UserRole.COMMON.value, comment='是否是超级管理员，可以管理所有的内容。')
    created_at = db.Column(db.DateTime, default=datetime.now, comment='创建时间')
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, comment='更新时间')


class UserProfile(db.Model):
    """ 用户的详细信息 """
    __tablename__ = 'accounts_user_profile'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 冗余字段
    username = db.Column(db.String(64), unique=True, nullable=False, comment='用户名')
    real_name = db.Column(db.String(64), comment='真实姓名')
    maxim = db.Column(db.String(128), comment='座右铭')
    sex = db.Column(db.String(16), comment='性别')
    address = db.Column(db.String(256), comment='地址')
    created_at = db.Column(db.DateTime, default=datetime.now, comment='创建时间')
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, comment='更新时间')

    user_id = db.Column(db.Integer, db.ForeignKey('accounts_user.id'), comment='关联用户')
    # 建立用户的一对一关系属性，user.profile profile.user
    #   backref 反向引用，就不需要再去 User 模型定义对应关系，但是通过 User 模型的实例也是可以获取对应的 profile 例：user.profile
    #   uselist 为 False 的话就是一对一的关系，True 就是一对多的关系。
    user = db.relationship('User', backref=db.backref('profile', uselist=False))


class UserLoginHistory(db.Model):
    __tablename__ = 'accounts_login_history'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), nullable=False, comment='用户名，用于登录')
    login_type = db.Column(db.String(32), comment='账号平台')
    ip = db.Column(db.String(32), comment='IP地址')
    ua = db.Column(db.String(128), comment='user-agent')
    created_at = db.Column(db.DateTime, default=datetime.now, comment='创建时间')
    user_id = db.Column(db.Integer, db.ForeignKey('accounts_user.id'), comment='关联用户')
    # 建立与用户的一对多属性，user.history_list
    user = db.relationship('User', backref=db.backref('history_list', lazy='dynamic'))


class Question(db.Model):
    """ 问题 """
    __tablename__ = 'qa_question'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128), nullable=False, comment='问题标题')
    desc = db.Column(db.String(256), comment='问题描述')
    img = db.Column(db.String(256), comment='问题图片')
    content = db.Column(db.Text, nullable=False, comment='问题详情')
    view_count = db.Column(db.Integer, default=0, comment='浏览人数')
    is_valid = db.Column(db.Boolean, default=True, comment='逻辑删除')
    reorder = db.Column(db.Integer, default=0, comment='排序')
    created_at = db.Column(db.DateTime, default=datetime.now, comment='创建时间')
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, comment='更新时间')
    user_id = db.Column(db.Integer, db.ForeignKey('accounts_user.id'), comment='关联用户')
    # 建立与用户一对多的属性，user.question_list
    user = db.relationship('User', backref=db.backref('question_list', lazy='dynamic'))


class QuestionTags(db.Model):
    """ 问题下的标签 """
    __tablename__ = 'qa_question_tags'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tag_name = db.Column(db.String(16), nullable=False, comment='标签名称')
    is_valid = db.Column(db.Boolean, default=True, comment='逻辑删除')
    created_at = db.Column(db.DateTime, default=datetime.now, comment='创建时间')
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, comment='更新时间')
    q_id = db.Column(db.Integer, db.ForeignKey('qa_question.id'), comment='关联问题')
    # 建立与问题一对多属性
    question = db.relationship('Question', backref=db.backref('tag_list', lazy='dynamic'))


class Answer(db.Model):
    """ 问题的回答 """
    __tablename__ = 'qa_answer'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False, comment='回答的内容详情')
    is_valid = db.Column(db.Boolean, default=True, comment='逻辑删除')
    created_at = db.Column(db.DateTime, default=datetime.now, comment='创建时间')
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, comment='更新时间')
    user_id = db.Column(db.Integer, db.ForeignKey('accounts_user.id'), comment='关联用户')
    q_id = db.Column(db.Integer, db.ForeignKey('qa_question.id'), comment='关联问题')
    # 建立与用户的一对多属性
    user = db.relationship('User', backref=db.backref('answer_list', lazy='dynamic'))
    # 建立与问题的一对多属性
    question = db.relationship('Question', db.backref('answer_list', lazy='dynamic'))


class AnswerComment(db.Model):
    """ 回答的评论 """
    __tablename__ = 'qa_answer_comment'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(512), nullable=False, comment='评论内容')
    love_count = db.Column(db.Integer, default=0, comment='赞同人数')
    is_public = db.Column(db.Boolean, default=True, comment='评论是否公开')
    is_valid = db.Column(db.Boolean, default=True, comment='逻辑删除')
    created_at = db.Column(db.DateTime, default=datetime.now, comment='创建时间')
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, comment='更新时间')
    reply_id = db.Column(db.Integer, db.ForeignKey('qa_answer_comment.id'), nullable=True, comment='回复ID')
    user_id = db.Column(db.Integer, db.ForeignKey('accounts_user.id'), comment='关联用户')
    answer_id = db.Column(db.Integer, db.ForeignKey('qa_answer.id'), comment='关联答案')
    q_id = db.Column(db.Integer, db.ForeignKey('qa_question.id'), comment='关联问题')
    # 建立与用户一对多的属性
    user = db.relationship('User', backref=db.backref('answer_comment_list', lazy='dynamic'))
    # 建立与答案一对多的属性
    answer = db.relationship('Answer', backref=db.backref('answer_comment_list', lazy='dynamic'))
    # 建立与问题一对多的属性
    question = db.relationship('Question', backref=db.backref('answer_comment_list', lazy='dynamic'))


class AnswerLove(db.Model):
    __tablename__ = 'qa_answer_love'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, default=datetime.now, comment='创建时间')
    user_id = db.Column(db.Integer, db.ForeignKey('accounts_user.id'), comment='关联用户')
    answer_id = db.Column(db.Integer, db.ForeignKey('qa_answer.id'), comment='关联答案')
    q_id = db.Column(db.Integer, db.ForeignKey('qa_question.id'), comment='关联问题')
    # 建立与用户的一对多属性
    user = db.relationship('User', backref=db.backref('answer_love_list', lazy='dynamic'))
    # 建立与答案的一对多属性
    answer = db.relationship('Answer', backref=db.backref('answer_love_list', lazy='dynamic'))
    # 建立与问题的一对多属性
    question = db.relationship('Question', backref=db.backref('question_love_list', lazy='dynamic'))


class AnswerCollect(db.Model):
    """ 收藏的回答 """
    __tablename__ = 'qa_answer_collect'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, default=datetime.now, comment='创建时间')
    is_valid = db.Column(db.Boolean, default=True, comment='逻辑删除')
    user_id = db.Column(db.Integer, db.ForeignKey('accounts_user.id'), comment='关联用户')
    answer_id = db.Column(db.Integer, db.ForeignKey('qa_answer.id'), comment='关联答案')
    q_id = db.Column(db.Integer, db.ForeignKey('qa_question.id'), comment='关联问题')
    # 建立与用户的一对多属性
    user = db.relationship('User', backref=db.backref('answer_collect_list', lazy='dynamic'))
    # 建立与问题的一对多属性
    question = db.relationship('Question', backref=db.backref('question_collect_list', lazy='dynamic'))
    # 建立与答案的一对多属性
    answer = db.relationship('Answer', backref=db.backref('answer_collect_list', lazy='dynamic'))


class QuestionFollow(db.Model):
    """ 关注的问题 """
    __tablename__ = 'qa_question_follow'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, default=datetime.now, comment='创建时间')
    is_valid = db.Column(db.Boolean, default=True, comment='逻辑删除')
    user_id = db.Column(db.Integer, db.ForeignKey('accounts_user.id'), comment='关联用户')
    q_id = db.Column(db.Integer, db.ForeignKey('qa_question.id'), comment='关联问题')
    # 建立与用户的一对多属性
    user = db.relationship('User', backref=db.backref('question_follow_list', lazy='dynamic'))
    # 建立与问题的一对多属性
    question = db.relationship('Question', backref=db.backref('question_follow_list', lazy='dynamic'))
