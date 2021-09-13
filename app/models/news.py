class News:
    '''
    News class to define News object
    '''
    def __init__(self,id,name,url,category,language,country):
        self.id = id
        self.name = name
        self.url = []
        self.category = category
        self.language = language
        self.country = country
    
        
        
        
class Article :
    '''
    Article class to define Article object
    '''
    def __init__(self,author,title,description,urlToImage,publishedAt,content):
        
        self.author = author
        self.title = title
        self.description = description
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content