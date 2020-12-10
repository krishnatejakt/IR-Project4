
import urllib.request
import re


def youtube_query(query):
    x = []
    
    if(query!='Trending'):
        html = urllib.request.urlopen("https://www.youtube.com/results?search_query="+query)
    else:
        html = html = urllib.request.urlopen("https://www.youtube.com/results?search_query=coronavirus")
    
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    count = 0
    for i in range(len(video_ids)):
        x.append("https://www.youtube.com/embed/" + video_ids[i])
        count+=1
        if(count==15):
            break
    return x

    #print(video_ids)
    #print("https://www.youtube.com/watch?v=" + video_ids[0])