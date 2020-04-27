import urllib.request,json
from .models import Sources, Articles

#Fetching the API Key
api_key = None

#Fetching the news base url
base_url = None

def configure_request(app):
  global api_key,base_url,article_base_url
  api_key = app.config['NEWS_API_KEY']
  base_url = app.config['NEWS_BASE_URL']

def get_source():
  '''
  Function that gets the json response to our url request
  '''
  get_source_url = base_url.format('sources', api_key)

  with urllib.request.urlopen(get_source_url) as url:
    get_source_data = url.read()
    get_sources_reponse = json.loads(get_source_data)

    source_results = None

    if get_sources_reponse['sources']:
      sources_results_list = get_sources_reponse['sources']
      source_results = process_results(sources_results_list)

  return source_results

def process_results(source_list):
  '''
  Processes the source results and converts them into a list of objects

  Args: 
    source_list: A list of dictionaries that contain different news sources

  Returns:
    source_results: A list of source objects
  '''
  sources_results = []

  for source_item in source_list:
    id = source_item.get('id')
    name = source_item.get('name')
    description = source_item.get('description')
    category = source_item.get('category')
    language = source_item.get('language')
    country = source_item.get('country')
    url = source_item.get('url')

    sources_results.append(Sources(id,name,description,category,language,country, url))

  return source_list

def get_articles(id):
  get_articles_url = base_url.format('everything',api_key) + '&sources='+ id

  with urllib.request.urlopen(get_articles_url) as url:
    get_articles_data = url.read()
    get_articles_response = json.loads(get_articles_data)

    articles_results = None

    if get_articles_response['articles']:
      articles_results_list = get_articles_response['articles']
      articles_results = process_articles_results(articles_results_list)

  return articles_results

def process_articles_results(articles_list):
  '''
  Function that process the articles and transforms them to a list of objects
  '''

  site_results =[]

  for article_item in articles_list:
    author = article_item.get('author')
    title = article_item.get('title')
    description = article_item.get('description')
    publishedAt = article_item.get('publishedAt')
    content = article_item.get('content')
    url = article_item.get('url')

    site_results.append(Articles(author,title,  description, publishedAt, content, url))

  return site_results

def search_news(topic):
  search_news_url = 'https://newsapi.org/v2/everything?q={}&apiKey={}'.format(topic, api_key)

  with urllib.request.urlopen(search_news_url) as url:
    search_news_data = url.read()
    search_response = json.loads(search_news_data)

    search_results = None

    if search_response['articles']:
      search_list = search_response['articles']
      search_results = process_search_results(search_list)

  return search_results
    