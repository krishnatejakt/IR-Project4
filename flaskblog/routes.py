from flaskblog.models import poi
from google_trans_new import google_translator
from flaskblog import app
from flaskblog.youtube import youtube_query
from flaskblog import db
import ast
from flask import render_template,url_for,flash,redirect,request
import json
from flaskblog.sentiment_analysis import sentiment_score
from flaskblog.newsapi import news
from flaskblog.models import poi
from flaskblog.forms import covid, poi_names, country, topic
from urllib.request import urlopen
from urllib.parse import urlparse
from langdetect import detect


ip_address = '54.175.73.162'

posts = []

query_news = []


#db.drop_all()

# db.create_all()

# result = db.engine.execute('select * from poi')
# results = []

# for row in result:
#     results.append(row)

@app.route('/')

@app.route('/home')

def home():
    data = urlopen('http://'+ip_address+':8983/solr/IRF20P1/select?q=*%3A*&sort=influencer_score%20desc%2C%20score%20desc&wt=json&rows=15')
    posts = json.load(data)['response']['docs']
    youtube_term = youtube_query('Trending')
    x = []
    for element in posts:
        name = element['user.screen_name'][0]
        element['user_name'] = name
        element['profile_image'] = element['user.profile_image_url'][0]
        x.append(element)
        element["sentiment_score"] = sentiment_score(element['full_text'][0].lower())

        query_news = news('Trending')
    return render_template('home.html',posts1='Trending Posts!',posts=posts,tests=query_news,youtube=youtube_term)
    
@app.route('/about')

def about():
    return render_template('about.html')

@app.route('/search',methods=['GET','POST'])

def search():
    gs = google_translator()
    form = covid()
    
    if form.validate_on_submit():

        youtube_search_term = ''
        news_search_term = ''
        x = []
        if(form.search.data==''):
            query_term='\"\"'
            query_term_dup = '\"\"'
        else:
            #print(type(form.search.data))
            query_term = form.search.data
            flash(f'Results for {form.search.data}!','success')

            if(detect(query_term)!='en'):
                query_term_dup = gs.translate(query_term,'en')
            else:
                query_term_dup = query_term
            #query_term_dup = gs.translate(query_term,'en')
            query_term = query_term.replace(' ','%20')
            query_term = query_term.encode("raw-unicode-escape").decode("utf-8") 
               
        
            
    
            #query_term = query_term.encode('utf-8')

        if(form.select.data==''):
            location='\"\"'
        else:
            location=form.select.data
        if(form.select1.data==''):
            poi='\"\"'
        else:
            poi = form.select1.data

    

        if(query_term_dup!='\"\"'):
             youtube_search_term+=query_term_dup+' '
             news_search_term+=form.search.data+' '

        if(poi!='\"\"'):
            youtube_search_term+=poi+' '
            news_search_term+=poi+' '

        if(location!='\"\"'):
            youtube_search_term+=location
            news_search_term+=location+' '



        youtube_search_term = youtube_search_term.replace(' ','%20')
        youtube_term = youtube_query(youtube_search_term)
        
        try:
            if(detect(form.search.data)!='en'):
                query_news = news(form.search.data)
            else:
                query_news = news(news_search_term)
        except:
            query_news = news(news_search_term)

        #print(news_search_term.encode('raw-unicode-escape').decode('utf-8'))

        youtube_search_term = '\"' + youtube_search_term + '\"'

        #print(youtube_search_term)

        data = urlopen('http://'+ip_address+':8983/solr/IRF20P1/select?defType=edismax&q=full_text%3A'+query_term+'%20AND%20user.screen_name%3A'+poi+'%20AND%20country%3A'+location+'&qf=full_text&sort=influencer_score%20desc%2C%20score%20desc&stopwords=true&rows=15&wt=json')
        #print('http://'+ip_address+':8983/solr/IRF20P1/select?defType=edismax&q=full_text%3A'+query_term+'%20AND%20user.screen_name%3A'+poi+'%20AND%20country%3A'+location+'&qf=full_text&sort=influencer_score%20desc%2C%20score%20desc&stopwords=true&wt=json&rows=15')
        posts = json.load(data)['response']['docs']


    
        for element in posts:
            try:
                name = element['user.screen_name'][0]
            except:
                name = 'User_has_no_name!'

            element['profile_image'] = element['user.profile_image_url'][0]
            element['user_name'] = name
            x.append(element)
            element["sentiment_score"] = sentiment_score(element['full_text'][0].lower())

        return render_template('home.html',posts=posts,tests=query_news,youtube=youtube_term)
            
        

    return render_template('search.html',form=form)

@app.route('/visualization')

def visualization():
    with open('static_json//static.json','r') as f:
        data = f.read()
    with open('static_json//correlation.json') as c:
        data1 = c.read()
    
    with open('static_json//pois_visualize.json') as m:
        data2 = m.read()

    items = json.loads(data)
    items1 = json.loads(data1)
    items2 = json.loads(data2)
    f.close()
    c.close()
    m.close()
    return render_template('visualization.html',items=items,items1=items1,items2=items2)

