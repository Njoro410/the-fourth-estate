import datetime
from flask import Blueprint, redirect,render_template,request,url_for
from .request import fetch_sources, get_articles, get_headlines, search_article



views = Blueprint('views',__name__)


@views.route('/')
def index():
    news_sources = fetch_sources('sources')
    print(news_sources)
    top_headlines = get_headlines('us')
    search_article = request.args.get('query')
    if search_article:
        return redirect(url_for('.search', query = search_article))
    else:
        return render_template('index.html',isIndex=True,sources=news_sources,headlines=top_headlines)


@views.route('/articles/<string:id>')
def articles(id):

    sources_articles = get_articles(id)
    print(sources_articles)
    date_now = datetime.datetime.now()
    

    return render_template('articles.html',articles=sources_articles,date= date_now)


@views.route('/search/<query>')
def search(query):
    '''
    View function to display the search results
    '''
    article_list = query.split(" ")
    article_list_format = "+".join(article_list)
    searched_articles = search_article(article_list_format)
    return render_template('search.html',s_articles=searched_articles)