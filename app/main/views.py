from flask import render_template
from . import main
from ..requests import get_source

@main.route('/')
@main.route('/Home')
def sources():
  """
  Page that displays the news sources as well as the link to articles and website
  """
  title = "Catch up with what has been happening around the globe"
  News_sources = get_source()

  return render_template('index.html',title=title,sources=News_sources)