import unittest
from app.models import Sources


class SourcesTest(unittest.TestCase):
  '''
  Test class to test the behavior of the sources class
  '''
  def setUp(self):
    '''
    Set up method that will run before every test
    '''
    self.new_source = Sources('bloomberg', 'Bloomberg News', 'Your trusted source for breaking news', 'general', 'us', 'en', 'https://abcnews.go.com')

  
  def test_instance(self):
    self.assertTrue(isinstance(self.new_source, Sources))
  
