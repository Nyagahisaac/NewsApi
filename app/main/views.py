from flask import render_template
from app import app

@app.route('/')
def index():
    
    '''
    View root page function that returns the index page and its data
    '''
   
    news_sources = get_news()
    
    
    # news_article = get_article()
    
    title = 'Home - Welcome to the best news Article Website online'
    return render_template('index.html',title = title, new_sources = news_sources)
