from flaskblog.models import poi
from flaskblog import app
from flaskblog import db
import ast
from flask import render_template,url_for,flash,redirect,request
import json
from flaskblog.sentiment_analysis import sentiment_score
from flaskblog.newsapi import news
from flaskblog.models import poi
from flaskblog.forms import covid, poi_names, country, topic
from urllib.request import urlopen



# with open('flaskblog//json_files//covid19 AND coronavirus AND government.json') as f:
#     data = f.read()

# data = data.replace('}{','},{')
# data = '[' + data + ']'
# posts = json.loads(data)
# f.close()


# for element in posts:
#     element['sentiment_score'] = sentiment_score(element['full_text'])


# query_news = news('x')

# for record in query_news:
#     record["sentiment_score"] = sentiment_score(record['abstract'])

posts = []

query_news = []


#db.drop_all()

db.create_all()

result = db.engine.execute('select * from poi')
results = []

for row in result:
    results.append(row)

@app.route('/')

@app.route('/home')

def home():
    return render_template('home.html',posts=posts,tests=query_news)
    
@app.route('/about')

def about():
    return render_template('about.html')

@app.route('/search',methods=['GET','POST'])
def search():
    form = covid()
    form1 = country()
    form2 = poi_names()
    form3 = topic()

    if form.validate_on_submit():
        if(form.search.data!=''):
            flash(f'Results for {form.search.data}!','success')
            x = []
            query_term = form.search.data
            query_term = query_term.replace(' ','%20')
            query_term_with_spaces = form.search.data

            data = urlopen('http://100.26.233.249:8983/solr/IRF20P4/select?defType=edismax&q=full_text%3A'+query_term+'&rows=20&sort=influencer_score%20desc&stopwords=true&wt=json')
            #print('http://100.25.155.102:8983/solr/IRF20P4/select?defType=edismax&q=full_text%3A'+query_term+'&rows=30&sort=influencer_score%20desc&stopwords=true')
            posts = json.load(data)['response']['docs']
            for element in posts:
                name = element['user'][0]
                name = json.loads(json.dumps(ast.literal_eval(name)))['name']
                element['user_name'] = name
                x.append(element)
                element["sentiment_score"] = sentiment_score(element['full_text'][0].lower())

            query_news = news(query_term)
            for record in query_news:
                record["sentiment_score"] = sentiment_score(record['abstract'])

            return render_template('home.html',posts=posts,tests=query_news)

    if form1.validate_on_submit():
        if(form1.select.data!=''):
            print(form1.select.data)
            #write
    if(form2.validate_on_submit()):
        if(form2.select.data!=''):
            pass
            #write
    if(form3.validate_on_submit()):
        if(form3.select.data!=''):
            pass
            #write
        

    return render_template('search.html',form=form,form1=form1,form2=form2,form3=form3)

@app.route('/visualization')

def visualization():
    with open('static_json//static.json','r') as f:
        data = f.read()

    items = json.loads(data)
    f.close()
    
    return render_template('visualization.html',items=items)

