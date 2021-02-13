from flask import Blueprint

from datetime import datetime
from flask import session
from .. import db

# article = Blueprint('article', __name__)

class Article(db.Model):
    __tablename__ = 'article'
    Id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    Title = db.Column(db.String(45), nullable=False)
    Abstract = db.Column(db.String(256), nullable=False)
    Content = db.Column(db.String(4096), nullable=False)
    Author = db.Column(db.String(45), nullable=False)
    CreateTime = db.Column(db.DateTime, default=datetime.now)
    ModifyTime = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, Title, Abstract, Content, Author):
        self.Title = Title
        self.Abstract = Abstract
        self.Content = Content
        self.Author = Author