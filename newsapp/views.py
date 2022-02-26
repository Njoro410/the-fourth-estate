from flask import Blueprint

views = Blueprint('views',__name__)

@views.route('/')
def index():
    return '<h1>welcome to news app</h1>'

@views.route('/sources')
def sources():
    return '<h1>list pf news sources</h1>'

@views.route('/top_headlines')
def top_headlines():
    return '<h1>top headlines around the world</h1>'
