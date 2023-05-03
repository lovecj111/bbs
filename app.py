from flask import Flask, render_template, session, g
from etc import config
from ext.exts import db
from blueprints.game import bp as game_bp
from blueprints.auth import bp as auth_bp
from flask_migrate import Migrate
from models import *

app = Flask(__name__)
app.config.from_object(config.BaseConfig)

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(game_bp)
app.register_blueprint(auth_bp)


@app.route('/')
def bbs():
    # https://github.com/hynever/flask_fullstack/tree/main/pythonbbs
    # flask db init
    # flask db migrate
    # flask db upgrade
    return render_template('success.html')


@app.before_request
def before_request():
    user_id = session.get('user_id')
    if user_id is not None:
        user = UserModel.query.get(user_id)
        setattr(g, 'user', user)
    else:
        setattr(g, 'user', None)


@app.context_processor
def context_processor():
    return {'user': g.user}


if __name__ == '__main__':
    app.run()
