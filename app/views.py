from flask import Blueprint,render_template,request
from .request import fetch_sources


views = Blueprint('views',__name__)

@views.route('/')
def index():
    news_sources = fetch_sources('sources')
    print(news_sources)

    return render_template('index.html',sources=news_sources)

@views.route('/sources')
def sources():


    return render_template('sources.html')

@views.route('/top_headlines')
def top_headlines():
    return render_template('top-headlines.html')
