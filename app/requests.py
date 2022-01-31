from concurrent.futures import process
import urllib.request, json
from .models import Sources, Articles

# Getting api key
api_key = None
# Getting the movie base url
base_url = None

def configure_request(app):
    '''
    function to configure requests
    '''
    global api_key, base_url,articles_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_SOURCES_BASE_URL']
    articles_url = app.config['ARTICLES_BASE_URL']

def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category, api_key)
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources(sources_results_list)

    return sources_results

def process_sources(sources_list):
    '''
    Function  that processes the news_sources result and transform them to a list of Objects
    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    sources_results = []

    for source_item in sources_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')

        sources_object = Sources(id,name,description,url,category,country,language)
        sources_results.append(sources_object)

    return sources_results


def get_articles(id):
    '''
	Function that processes the articles and returns a list of articles objects
	'''
    get_articles_url = articles_url.format(id,api_key)
    
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        articles_results = json.loads(get_articles_data)

        articles_object = None
        
        if articles_results['articles']:
            articles_object = process_articles(articles_results['articles'])
        
        return articles_object

def process_articles(articles_list):
	'''
    Function to process articles list and return 
	'''
	articles_object = []

	for article_item in articles_list:
		id = article_item.get('id')
		author = article_item.get('author')
		title = article_item.get('title')
		description = article_item.get('description')
		url = article_item.get('url')
		image = article_item.get('urlToImage')
		date = article_item.get('publishedAt')
		
		if image:
			articles_result = Articles(id,author,title,description,url,image,date)
			articles_object.append(articles_result)	

	return articles_object