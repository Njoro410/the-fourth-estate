from flask import Blueprint,render_template,request
from .request import fetch_sources, get_articles


views = Blueprint('views',__name__)


@views.route('/')
def index():
    news_sources = fetch_sources('sources')
    print(news_sources)

    return render_template('index.html',sources=news_sources)


@views.route('/articles/<string:id>')
def articles(id):

    sources_articles = get_articles(id)
    print(sources_articles)

    return render_template('articles.html',articles=sources_articles)
