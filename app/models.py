class Sources:
  '''
  Defines sources objects

  '''
  def __init__(self, id, name, description, category, language, country, url):
    self.id = id
    self.name = name
    self.description = description
    self.category = category
    self.country = country
    self.language = language
    self.url = url

class Articles:
  '''
  Defines article objects

  '''
  def __init__(self, author, title, description, publishedAt, content, url, urlToImage):
    self.author = author
    self.title = title
    self.description = description
    self.publishedAt = publishedAt
    self.content = content
    self.url = url
    self.urlToImage = urlToImage

class Topic:
  '''
  Topic class to define Topic objects
  '''

  def __init__(self,author,title,description,url,urlToImage,publishedAt):

    self.author = author
    self.title = title
    self.description = description
    self.url = url
    self.urlToImage = urlToImage
    self.publishedAt = publishedAt

