from app import app
import urllib.request,json
from .models import news,article

# from .models import article

News = news.News
Article = news.Article

# api_key = app.config['NEWS_API_KEY']
base_url = app.config["ARTICLE_API_BASE_URL"]
sources_url = app.config['NEWS_SOURCES']

def get_news():
    '''
    Function that gets the json response to url request
    '''
    get_news_url = sources_url
    print('--------------------')
    print(get_news_url)
    print('--------------------')
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        
        news_results = None
        
        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)
            
    return news_results






def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of movie objects
        
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        url = news_item.get('url')
        category = news_item.get('category')
        language = news_item.get('language')
        country = news_item.get('country')

        if url:
            news_object = News(id,name,url,category,language,country)
            news_results.append(news_object)

    return news_results

    
    
    
    
    
    
    
    
    
def get_article(id):
    '''
    Function that gets the json response to url request
    '''
    get_article_url = base_url.format(id)
    
    with urllib.request.urlopen(get_article_url) as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)
        
        article_results = None
        
        if get_article_response['articles']:
            
            print('Okay')
            article_results_list = get_article_response['articles']
            article_results = proccess_results(article_results_list)
            
    return article_results

def proccess_results(article_list):
    '''
    Function  that processes the Article result and transform them to a list of Objects

    Args:
        article_list: A list of dictionaries that contain news details

    Returns :
        article_results: A list of movie objects
        
    '''
    article_results = []        
    for news_item in article_list:
        
        author = news_item.get('author')
        title = news_item.get('title')
        description = news_item.get('description')
        urlToImage = news_item.get('urlToImage')
        publishedAt = news_item.get('publishedAt')
        content = news_item.get('content')

        if author:
            print('Tested')
            news_object = Article(author,title,description,urlToImage,publishedAt,content)
            article_results.append(news_object)

    return article_results