from flask import render_template
from app import app
from ..request import get_news,get_article
# from progressbar  import  NgProgressModule
# from progressbar  import NgProgressHttpClientModule 


...

@app.route('/')
def index():
    
    '''
    View root page function that returns the index page and its data
    '''
   
    news_sources = get_news()
    
    
    # news_article = get_article()
    
    title = 'Home - Welcome to the best news Article Website online'
    return render_template('index.html',title = title, new_sources = news_sources)
















@app.route('/news/<string:new_id>')
def news(new_id):
    
    '''
    View news page function that returns the news details page and its data 
    '''
    news = get_article(new_id)
    print('----------------')
    print(new_id)
    print('----------------')
    return render_template('article.html', news = news)

# @app.route('/article/<int:article_id>')
# def article(id):
#     '''
#     View article page function that returns the article details page and its data
#     '''
    
#     article = get_article(id)
#     author = f'{article.author}'
#     return render_template('article.html',author = author)
    
    