import urllib.request,json
from .models import Sources

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
