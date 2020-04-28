import urllib.request,json
from .models import Sources, Articles, Topic

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
  get_source_url = base_url.format('sources', api_key) + '&language=en'

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
    

    source_object = Sources(id,name,description,category,language,country, url)
    sources_results.append(source_object)

  return sources_results

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
    urlToImage = article_item.get('urlToImage')

    if urlToImage:
      article_object = Articles(author, title, description, publishedAt, content, url, urlToImage)
    else: 
      article_object = Articles(author, title, description, publishedAt, content, url)

    site_results.append(article_object)

  return site_results
 
def get_topic(topic_news):
  get_topic_url = base_url.format('everything',api_key) + '&q=' + topic_news

  with urllib.request.urlopen(get_topic_url) as url:
    get_topic_data = url.read()
    get_topic_response = json.loads(get_topic_data)

    news_topic_results = None

  if get_topic_response['articles']:
    topic_results_list = get_topic_response['articles']
    news_topic_results = process_topic_results(topic_results_list)
      
  return news_topic_results

def process_topic_results(topic_list):
  '''
  Function that process the topics and transforms them to a list of objects
  '''

  topic_results = []
  for topic_item in topic_list:
    author = topic_item.get('author')
    title = topic_item.get('title')
    description = topic_item.get('description')
    url = topic_item.get('url')
    urlToImage = topic_item.get('urlToImage')
    publishedAt = topic_item.get('publishedAt')

    topic_results.append(Topic(author,title,description,url,urlToImage,publishedAt))

  return topic_list

def search_news(topic_news):
  search_news_url = 'https://newsapi.org/v2/everything?apiKey={}&q={}'.format(api_key,topic_news)

  with urllib.request.urlopen(search_news_url) as url:
    search_news_data = url.read()
    search_news_response = json.loads(search_news_data)

    search_news_results = None


    if search_news_response['articles']:
      search_news_list = search_news_response['articles']
      search_news_results = process_topic_results(search_news_list)

  return search_news_results

