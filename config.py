class Config:
    '''
    General configuration parent class 
    '''
    
    ARTICLE_API_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey=9697425881ce4e618ee8df65c57dc95c'
    NEWS_SOURCES='https://newsapi.org/v2/sources?apiKey=9697425881ce4e618ee8df65c57dc95c'
    
class ProdConfig(Config):
    '''
    Production configuration child class
    
    Args:
        Config:The parent configuration class with General configuration settings 
    '''
    pass













class DevConfig(Config):
    '''
    Development configuration child class 
    
    Args:
        Config:The parent configuration class with General configuration settings 
    '''
    DEBUG = True
