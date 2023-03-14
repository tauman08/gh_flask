from flask_login import UserMixin
from blog.app import db
from werkzeug.security import check_password_hash

class User(db.Model,UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(255), unique = True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    password = db.Column(db.String(255))

    def __init__(self, email, first_name, last_name, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password, password)