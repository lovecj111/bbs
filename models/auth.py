from ext.exts import db


class UserModel(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(20), nullable=False)
    pass_word = db.Column(db.String(20), nullable=True)
