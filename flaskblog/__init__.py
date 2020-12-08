from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flaskblog.sentiment_analysis import sentiment_score
from flaskblog.newsapi import news
import json


app = Flask(__name__)
app.config['SECRET_KEY'] = 'e9d5c09882a2cc242cd83607b251b3be'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app) #create instance
from flaskblog import routes

