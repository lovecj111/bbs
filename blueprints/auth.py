from flask import Blueprint, render_template, request, redirect, url_for, session

from blueprints.forms.register_form import RegisterForm
from blueprints.forms.login_form import LoginForm
from models.auth import UserModel
from ext.exts import db

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        form = RegisterForm(request.form)
        if form.validate():
            user_name = form.username.data
            pass_word = form.password1.data
            user = UserModel(user_name=user_name, pass_word=pass_word)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("auth.login"))
        else:
            return redirect(url_for("auth.register"))


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        form = LoginForm(request.form)
        if form.validate():
            user_name = form.username.data
            pass_word = form.password.data
            user = UserModel.query.filter_by(user_name=user_name, pass_word=pass_word).first()
            if user is None:
                return redirect(url_for("auth.login"))
            session['user_id'] = user.id
            return redirect("/")
        else:
            return redirect(url_for("auth.login"))


@bp.route('/logout')
def logout():
    session.clear()
    return redirect("/")
