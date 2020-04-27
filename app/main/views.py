from flask import render_template, redirect, request, url_for
from . import main
from ..requests import get_source, get_articles, search_news, get_topic
from datetime import datetime




@main.app_template_filter('datetimeformat')
def datetimeformat(value, format='%B'):
  '''
  Formats dates to a more readable format 

  '''
  return datetime_object.strftime ( format)

@main.route('/')
@main.route('/home')
def index():
  """
  Page that displays the news sources as well as the link to articles and website
  """
  title = "Keep up with all the topics that matter to you. All in one place"
  sources = get_source()

  search_news = request.args.get('news_query')

  if search_news:
    return redirect(url_for('main.search', topic = search_news))
  else:
    return render_template('index.html', title=title, sites=sources)

@main.route('/articles/<id>')
def articles(id):
  '''
  Page that displays a list of articles from a given source

  '''
  source_articles = get_articles(id)
  title = 'News articles'

  search_news = request.args.get('news_query')

  if search_news:
    return redirect(url_for('main.search',topic = search_news))
  else:
    return render_template('source_details.html',title=title,details=source_articles)

@main.route('/search/<topic>')
def search(topic):
  '''
  View function to display the search results
  '''

  news_name_list = topic.split(' ')
  news_name_format = '+'.join(news_name_list)
  searched_topics = get_topic(news_name_format)
  title = f'search results for {topic}'

  search_news = request.args.get('news_query')

  if search_news:
    return redirect(url_for('main.search',topic = search_news))
  else:
    return render_template('search_results.html',news_topics = searched_topics, t =topic,title=title)
