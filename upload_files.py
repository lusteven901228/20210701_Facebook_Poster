import requests
from pie import plot_pie, get_time
import json
import os
t = open('config.json')
data = json.load(t)
user_access_token = data['user_access_token']
page_id = data['page_id']
p_response = requests.get('https://graph.facebook.com/'+ page_id + '?fields=access_token&access_token='+user_access_token)
page_access_token = p_response.json()['access_token']
t.close()
url = 'https://graph.facebook.com/'+page_id+'/'
def upload(x):
    yr = str(2000+x//1000)
    percent = str((x%1000)/10)
    plot_pie(x)
    img_data = {'published':'false','temporary':'true','access_token':page_access_token}
    respond = requests.post(url+'photos',data = img_data,files = {'source':(open(str(x)+'.jpg','rb'))})
    id = respond.json()['id']
    r = requests.post(
    'https://graph.facebook.com/106447670161953/feed?access_token='+page_access_token,data = {
    'message':f'''{yr}已經過了{percent}%\n{percent}% of year {yr} has passed.''',
    'attached_media[0]':'{"media_fbid":'+id+'}',
    'access_token':page_access_token,
    'published':'false',
    'scheduled_publish_time':get_time(x),
    'unpublished_content_type':'SCHEDULED'
    }
    )
    print(r.json())
    os.system("del /f "+str(x)+'.jpg')
if __name__ == '__main__':
    upload(int(input('x')))
