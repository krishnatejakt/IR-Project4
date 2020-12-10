from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from google_trans_new import google_translator

analyser = SentimentIntensityAnalyzer()

def sentiment_score(text):
    gs = google_translator()
    text = gs.translate(text,'en')
    return analyser.polarity_scores(text)['compound']
    
