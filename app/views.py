import datetime
from flask import Blueprint,render_template,request
from .request import fetch_sources, get_articles, get_headlines



views = Blueprint('views',__name__)


@views.route('/')
def index():
    news_sources = fetch_sources('sources')
    print(news_sources)
    top_headlines = get_headlines('us')

    return render_template('index.html',sources=news_sources,headlines=top_headlines)


@views.route('/articles/<string:id>')
def articles(id):

    sources_articles = get_articles(id)
    print(sources_articles)
    date_now = datetime.datetime.now()
    

    return render_template('articles.html',articles=sources_articles,date= date_now)


