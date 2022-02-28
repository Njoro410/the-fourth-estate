import urllib.request
import json
from .models import Sources, Articles, Top

# get API key
api_key = None

# get base url
base_url = None

#get articles_url
articles_url = None

#get top_url
top_url = None



def configure_request(app):
    global api_key, base_url,articles_url,top_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    articles_url = app.config['ARTICLES_API_BASE_URL']
    top_url = app.config['TOP_URL']


    

def fetch_sources(category):
    """
    method to get JSON response for sources
    """
    get_sources_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_results(sources_results_list)

    return sources_results


def process_results(sources_list):
    """
    Method to return results and transform them to a list of objects

    Args:   sources_list: A list of dictionaries that has info about sources

    Method retuns {sources_results} which is a list of sources objects
    """

    sources_results = []
    for source_item in sources_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('catgeory')
        language = source_item.get('language')
        country = source_item.get('country')

        sources_object = Sources(
            id, name, description, url, category, language, country)
        sources_results.append(sources_object)

    return sources_results


def get_articles(source):
    get_source_article_url = articles_url.format(source, api_key)
    

    with urllib.request.urlopen(get_source_article_url) as url:
        article_details_data = url.read()
        article_details_response = json.loads(article_details_data)

        article_results = None

        if article_details_response['articles']:
            article_results_list = article_details_response['articles']
            article_results = process_articles(article_results_list)

    return article_results


def process_articles(article_list):
    '''
    Function  that processes the article results and transform them to a list of Objects

    Args:
        article_list: A list of dictionaries that contain article details

    Returns :
        article_results: A list of article objects
    '''

    article_results = []
    for article_item in article_list:
        id = article_item.get('id')
        name = article_item.get('name')
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
        content = article_item.get('content')

        article_object = Articles(id,name,author,title,description,url,urlToImage,publishedAt,content)
        article_results.append(article_object)
    return article_results



def get_headlines(country):
    get_headline_url = top_url.format(country, api_key)
    

    with urllib.request.urlopen(get_headline_url) as url:
        headline_details_data = url.read()
        headline_details_response = json.loads(headline_details_data)

        headline_results = None

        if headline_details_response['articles']:
            headline_results_list = headline_details_response['articles']
            headline_results = process_articles(headline_results_list)

    return headline_results


def process_headlines(headline_list):
    '''
    Function  that processes the article results and transform them to a list of Objects

    Args:
        article_list: A list of dictionaries that contain article details

    Returns :
        article_results: A list of article objects
    '''

    headline_results = []
    for headline_item in headline_list:
        id = headline_item.get('id')
        name = headline_item.get('name')
        author = headline_item.get('author')
        title = headline_item.get('title')
        description = headline_item.get('description')
        url = headline_item.get('url')
        urlToImage = headline_item.get('urlToImage')
        publishedAt = headline_item.get('publishedAt')
        content = headline_item.get('content')

        headline_object = Top(id,name,author,title,description,url,urlToImage,publishedAt,content)
        headline_results.append(headline_object)
    return headline_results








