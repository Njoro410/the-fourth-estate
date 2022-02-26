from flask import Blueprint,render_template

views = Blueprint('views',__name__)

@views.route('/')
def index():
    return render_template('index.html')

@views.route('/sources')
def sources():
    return render_template('sources.html')

@views.route('/top_headlines')
def top_headlines():
    return render_template('top-headlines.html')
