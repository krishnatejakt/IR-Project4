import json
import requests


def news(query):
    # news_query = requests.get('https://api.nytimes.com/svc/search/v2/articlesearch.json?q='+query+'&api-key=KsLEcgWEJLqIkK2hdacjklZiPyHyOxLh&sort=newest&page=0') # (your url)
    # data = news_query.json()
    # return data['response']['docs']
    # return data['response']['docs']

    if(query!='Trending'):
        url = ('http://newsapi.org/v2/everything?'
        'q='+query+'&'
        'from=2020-11-17&'
        'sortBy=popularity&'
        'apiKey=8ab0444ae6e74d0eb01c52f941647514&'
        'pageSize=15')
    else:
        url = url = ('http://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=8ab0444ae6e74d0eb01c52f941647514&'
       'pageSize=15')

    try:
        response = requests.get(url)
        data = json.loads(json.dumps(response.json()))

        return data['articles']
    except:
        return []
