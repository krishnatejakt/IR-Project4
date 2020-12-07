import json
import requests

def news(query):
    news_query = requests.get('https://api.nytimes.com/svc/search/v2/articlesearch.json?q='+query+'&api-key=KsLEcgWEJLqIkK2hdacjklZiPyHyOxLh') # (your url)
    data = news_query.json()
    return data['response']['docs']
