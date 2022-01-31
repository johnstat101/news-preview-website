from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_sources, get_articles
from ..models import Sources, Articles

# views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    # Getting sources by category 
    business = get_sources('business')
    sports = get_sources('sports')
    technology = get_sources('technology')
    entertainment = get_sources('entertainment')

    title = 'News Previews Website'
    
    return render_template('index.html', title = title, business = business, sports = sports, technology = technology, entertainment = entertainment)


@main.route('/sources/<int:id>')
def articles(id):

    '''
    View articles page function that returns articles in a given sources
    '''
    article = get_articles(id)
    title = f'{article.title}'

    return render_template('articles.html',title = title,article = article)