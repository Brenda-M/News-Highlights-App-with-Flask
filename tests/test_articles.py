import unittest
from app.models import Articles


class ArticlesTest(unittest.TestCase):
  '''
  Test class to test the behavior of the articles class
  '''
  def setUp(self):
    '''
    Set up method that will run before every test
    '''
    self.new_article = Articles('Catie', 'Travelex Reportedly Paid Ransomware Hackers 285 Bitcoin', 'Following a ransomware attack against foreign exchange company Travelex earlier this year', '2020-04-09T21:40:00Z', 'Following a ransomware attack against foreign exchange company Travelex earlier this year', 'https://gizmodo.com/travelex-reportedly-paid-ransomware-hackers-285-bitcoin-1842782514', 'https://abcnews.go.com')

  
  def test_instance(self):
    self.assertTrue(isinstance(self.new_article, Articles))