## Project Name

News Highlights Application

## Author Information

Muthoni Njuguna

## Description

This is a flask web application that allows users access to various news sources from all around the world. In this way, a user can keep track and stay in touch with the latest information


## User Stories

As a user, you will be able to:

  1. See various news sources on the homepage of the application. 
  2. Select a news source and see all news articles from the selected news.
  3. See the image, description and the time a news article was created.
  4. Click on an article and read the full article on the source website.
  5. Search for an article on a specific topic

## Technologies Used

  Python
  Flask 

## BBD

| Behaviour	|Input | Output|
|--------------|------------|------------|
|On the site|	Click a source|	Redirects to site|
|Read article on site	|Click on 'Read more..'	|Takes you to article on site
|Search for news	|Click on search button	|News with keyword is displayed

## Setup/Installation Requirements

Before running this application on your local machine, ensure that you have python3 and pip installed on your computer.
Once you are done with the step above, proceed to clone the application by running git clone https://github.com/Brenda-M/News-Highlights-App-with-Flask.git on the teminal.

## Installing Required Modules

$ python3.6 -m pip install Flask
$ python3.6 -m pip install Flask-Bootstrap
$ python3.6 -m pip install Flask-Script

## Setting up ApiKey and Running the App

  1. Visit https://newsapi.org/ and register for an API key.
  2. Create a start.sh file in the projects rrot directory.
  3. Add "export NEWS_API_KEY='<your_api_key>'"  and python3.6 manage.py server in the file. 
  4. Make the file executable by running $ chmod a+x start.sh on the terminal
  5. Run application using $ ./start.sh


## Contact Information

In case of any feedback, you can reach me through: -brendanjuguna1@gmail.com

## License

The MIT License (MIT) Copyright (c) 2020 Muthoni Njuguna.