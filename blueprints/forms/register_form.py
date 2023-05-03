import wtforms
from wtforms.validators import Length, EqualTo


class RegisterForm(wtforms.Form):
    username = wtforms.StringField(validators=[Length(min=3, max=20, message="用户名长度不正确!")])
    password1 = wtforms.StringField(validators=[Length(min=6, max=20, message="密码长度不正确!")])
    password2 = wtforms.StringField(validators=[EqualTo("password1", message="两次密码不一致")])
