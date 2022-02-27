import urllib.request
import json
from .models import Sources, Articles

# get API key
api_key = None

# get base url
base_url = None


def configure_request(app):
    global api_key, base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']


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
