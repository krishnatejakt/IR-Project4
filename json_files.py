#replace filenames and index them in solr
with open('Desktop\\flaskIR\\flaskblog\\json_files\\covid19 AND coronavirus AND government.json') as f:
    data = f.read()
data = data.replace('}{','},{')
data = '['+data+']'
import json
x = json.loads(data)

for element in x:
    try:
        element["influencer_score"] = (element["retweet_count"]+element["favorite_count"])/element["user"]["followers_count"]
    except:
        element["influencer_score"] = 0
    element["sentiment_score"] = sentiment_score(element["full_text"])

#replace filenames.
with open('sample.json','w') as f:
    json.dump(x,f,indent=4)