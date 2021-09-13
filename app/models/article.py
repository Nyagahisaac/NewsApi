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
        