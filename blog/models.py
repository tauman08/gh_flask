from flask_login import UserMixin
from blog.app import db
from werkzeug.security import check_password_hash
from sqlalchemy import ForeignKey, Table, Column
from sqlalchemy.orm import relationship
from datetime import datetime


articale_tag_associations_table = Table(
    'articale_tag_associations',
    db.metadata,
    db.Column('articale_id', db.Integer, ForeignKey(
        'articles.id'), nullable=False),
    db.Column('tag_id', db.Integer, ForeignKey('tags.id'), nullable=False),
)


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    # можно и нужно писать так :
    # email = Column(db.String(255), unique=True)
    email = db.Column(db.String(255), unique=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    password = db.Column(db.String(255))
    is_staff = db.Column(db.Boolean, default=False)

    author = relationship('Author', uselist=False, back_populates='user')

    def __init__(self, email, first_name, last_name, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password, password)

    def __str__(self):
        return f'{self.email} {self.first_name} {self.last_name}'


class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey("users.id"), nullable=False)

    user = relationship('User', back_populates='author')
    article = relationship('Article', back_populates='author')

    def __str__(self):
        return self.user.email


class Article(db.Model):
    __tablename__ = 'articles'
    # лучше определять колонки не через экземпляр класса db.column а через класс sqlalchemy чтобы не было проблемы
    # с циклическими ссылками. Как у нас было в начале
    id = Column(db.Integer, primary_key=True)
    author_id = Column(db.Integer, ForeignKey('authors.id'), nullable=False)
    title = Column(db.String(255))
    text = Column(db.Text)
    created_at = Column(db.DateTime, default=datetime.utcnow)
    updated_at = Column(db.DateTime, default=datetime.utcnow,
                        onupdate=datetime.utcnow)

    author = relationship('Author', back_populates='article')
    tags = relationship(
        'Tag', secondary=articale_tag_associations_table, back_populates='articles')

    def __str__(self):
        return self.title


class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    articles = relationship(
        'Article', secondary=articale_tag_associations_table, back_populates='tags')

    def __str__(self):
        return self.name
