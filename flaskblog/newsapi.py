import json
import requests

def news(query):
    # news_query = requests.get('https://api.nytimes.com/svc/search/v2/articlesearch.json?q='+query+'&api-key=KsLEcgWEJLqIkK2hdacjklZiPyHyOxLh&sort=newest&page=0') # (your url)
    # data = news_query.json()
    # return data['response']['docs']

    url = ('http://newsapi.org/v2/everything?'
       'q='+query+'&'
       'from=2020-11-12&'
       'sortBy=popularity&'
       'apiKey=8ab0444ae6e74d0eb01c52f941647514&'
       'page=1')

    try:
        response = requests.get(url)
        data = json.loads(json.dumps(response.json()))

        return data['articles']
    except:
        return []
