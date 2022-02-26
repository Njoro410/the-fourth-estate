from flask import Blueprint,render_template

views = Blueprint('views',__name__)

@views.route('/')
def index():
    return render_template('index.html')

@views.route('/sources')
def sources():
    return '<h1>list pf news sources</h1>'

@views.route('/top_headlines')
def top_headlines():
    return '<h1>top headlines around the world</h1>'
