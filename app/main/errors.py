from flask import render_template
from . import main

@main.app_errorhandler(404)
def page_not_found(error):
  '''
  Renders a 404 page when a page cannot be found

  '''
  return render_template('pageNotFound.html'), 404