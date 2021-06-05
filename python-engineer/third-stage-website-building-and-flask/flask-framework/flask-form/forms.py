import re

from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, DateField, IntegerField, FileField
from wtforms.validators import DataRequired, ValidationError


def phone_required(form, field):
    """ 自定义的手机号码验证 """
    # 强制验证用户名为手机号
    username = field.data
    pattern = r'^1[0-9]{10}$'
    if not re.search(pattern, username):
        raise ValidationError('用户名只能为手机号码')
    return field


class LoginForm(FlaskForm):
    """ 登录表单的实现 """
    """
        表单字段的常用核心参数
            label       label 标签（如：如输入框前的文字描述）
            default     表单的默认值
            validators  表单的验证规则
            widget      定制界面显示方式（如：文本框、选择框）
            description 帮助文字

        表单渲染
            使用模板语法渲染表单内容
                表单输入区域：{{ form.username }}
                表单 label ：{{ form.username.label.text }}
                
        表单常用字段类型
            文本/字符串
                StringField     字符串输入
                PasswordField   密码输入
                TextAreaField   长文本输入
                HiddenField     隐藏表单域
            数值（整数，小数）
                FloatField      浮点数输入
                IntegerField    整数输入
                DecimalField    小数输入（更精确）
            选择
                RadioField      radio 单选
                SelectField     下拉单选
                SelectMultipleField 下拉多选
                BooleanField    勾选（复选框）
            日期
                DateField       日期选择
                DateTimeField   日期时间选择
            文件
                FileField       文件单选
                MultipleFileField   文件多选
            其他
                SubmitField     提交按钮
                FieldList       自定义的表单选择列表（如：选择用户对象）
                FormField       自定义多个字段构成的选项
    """
    username = StringField(label='用户名', validators=[phone_required])
    password = PasswordField(label='密码', validators=[DataRequired('请输入密码')])
    submit = SubmitField(label='登录')


class RegisterForm(FlaskForm):
    """ 用户注册表单 """
    username = StringField(label='用户名')
    password = PasswordField(label='密码', validators=[DataRequired('请输入密码')])
    birthday = DateField(label='生日')
    age = IntegerField(label='年龄')
    submit = SubmitField(label='注册')

    # 加下面这句是为了屏蔽 Pycharm 提示 "Method 'validate_username' may be 'static'"
    # noinspection PyMethodMayBeStatic
    # 名字命名是有要求的 validate 加 对应要验证的字段
    def validate_username(self, field):
        """ 验证用户名 """
        # 强制验证用户名为手机号
        username = field.data
        pattern = r'^1[0-9]{10}$'
        if not re.search(pattern, username):
            raise ValidationError('用户名只能为手机号码')
        return field


class UserAvatarForm(FlaskForm):
    avatar = FileField(label='上传头像', validators=[
        FileRequired('请选择头像文件'),
        FileAllowed(['png', 'jpeg'], '文件的后缀不符合要求')
    ])
