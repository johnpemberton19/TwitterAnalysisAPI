import urllib
import urllib2
import re
import json

ClientId = '5aed54fedcea4289a5f1515f996a15a3'
ClientSecret = '80897f072eda42cc9b32fefa901ac126'
WebsiteURL = 'http://www.catchtrend.co.nf/Blog/'
InstagramAPI = 'https://api.instagram.com/v1/'

def search(tag):
    imagelist = []
    url = 'https://api.instagram.com/v1/tags/'+tag+'/media/recent?min_id=0&client_id='+ClientId
    aResp = urllib2.urlopen(url)
    web_pg = aResp.read()
    pattern = 'url(.+?)jpg'
    jdict = json.loads(web_pg)
    for i in range(len(jdict['data'])):
        imagelist.append(jdict['data'][i]['images'].values()[0]['url'].encode('utf-8'))
    return imagelist
    
