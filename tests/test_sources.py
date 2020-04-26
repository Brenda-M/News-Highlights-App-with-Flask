import unittest
from app.models import Source


class SourcesTest(unittest.TestCase):
  '''
  Test class to test the behavior of the news class
  '''
  def setup(self):
    '''
    Set up method that will run before every test
    '''
    self.new_source = Source('bloomberg', 'Bloomberg News', 'Your trusted source for breaking news', 'general', 'us', 'en', 'https://abcnews.go.com')

  
  def test_instance(self):
    self.assertTrue(isinstance(self.new_news, Source))
  
  if __name__ == '__main__':
    unittest.main()
