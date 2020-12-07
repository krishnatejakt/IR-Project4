from flaskblog import db


with open('flaskblog//json_files//@narendramodi.json',encoding = 'utf-8') as f:
    data = f.read()
    
data = data.replace('}{','},{')
data = '[' + data + ']'
narendra_modi = json.loads(data)

result = db.engine.execute('select count(*) from poi')

for row in result:
    count = row[0]
if(count==0):   
    for tweet in narendra_modi:
        try:
            sample_tweet = poi(username='Narendra Modi',country='India',text=tweet['full_text'],unique_id=tweet['id'])
            db.session.add(sample_tweet)
            db.session.commit()
        except:
            pass

    f.close()