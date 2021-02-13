from flask import Blueprint
from flask import jsonify
from ..model.Article import Article
from .. import db

myapi = Blueprint('myapi', __name__)
# api = Api(myapi)

@myapi.route('/queryArticle')
def QueryArticle():
    resJsonArr = []
    query = Article.query.order_by(Article.Id.asc()).all()
    print('asc : ')
    for q in query:
        jsonObj = {}
        jsonObj['Id'] = q.Id
        jsonObj['Title'] = q.Title
        jsonObj['Abstract'] = q.Abstract
        jsonObj['Content'] = q.Content
        jsonObj['Author'] = q.Author
        jsonObj['CreateTime'] = q.CreateTime
        resJsonArr.append(jsonObj)
        print(jsonObj)
    return jsonify(resJsonArr)

@myapi.route('/api_1')
def api_1():
    return 'THIS IS API 1'

@myapi.route('/api_2')
def api_2():
    return 'THIS IS API 2'
