from twitter import *
import re
import urllib
import urllib2


gd = {'good':1,
          'great':1,
          'wonderful':1,
          'fantastic':1,
          'awesome':1,
          'perfect':1,
          'better':1,
          'best':1,
          'woo hoo':1,
          'incredible':1,
          'positive':1,
          'happy':1,
          'excited':1
          }

bd = {'bad':-1,
          'horrible':-1,
          'aweful':-1,
          'crap':-1,
          'disgusting':-1,
          'horrid':-1,
          'annoying':-1,
          'worse':-1,
          'yuck':-1,
          'sad':-1,
          'mad':-1,
          'angry':-1
          }


t = Twitter(auth = OAuth('2392087700-jt71UOdz7nOOwO6aylppNDVhcLwgErig5BuZZGv', 'tGT4BgU1N8gJqrR0qgUvwdfW2FzjFiLTQLjq8aQqmVL9t', 'sSfVfvJ8wMZ6erCeejDzw', '0xNLZ82pfI5z5iaJMYF6gZhoYs1qYnwYpqG74e0TUM'))

def Twitter_auth():
    t = Twitter(auth = OAuth('2392087700-jt71UOdz7nOOwO6aylppNDVhcLwgErig5BuZZGv', 'tGT4BgU1N8gJqrR0qgUvwdfW2FzjFiLTQLjq8aQqmVL9t', 'sSfVfvJ8wMZ6erCeejDzw', '0xNLZ82pfI5z5iaJMYF6gZhoYs1qYnwYpqG74e0TUM'))

def Twitter_getmystatuses():
    x = t.statuses.user_timeline(screen_name='johnpemberton19')
    for i in range(len(x)):
	print x[i]['text'].encode('utf-8')

def Twitter_creategood_dictionary():
    gd = {'good':1,
          'great':1,
          'wonderful':1,
          'fantastic':1,
          'awesome':1,
          'perfect':1,
          'better':1,
          'best':1,
          'woo hoo':1,
          'incredible':1,
          'positive':1,
          'happy':1,
          'excited':1
          }

def Twitter_createbad_dictionary():
     bd = {'bad':-1,
          'horrible':-1,
          'aweful':-1,
          'crap':-1,
          'disgusting':-1,
          'horrid':-1,
          'annoying':-1,
          'worse':-1,
          'yuck':-1,
          'sad':-1,
          'mad':-1,
          'angry':-1
          }

def Twitter_getmystatuses_inwords():
    x = t.statuses.user_timeline(screen_name='johnpemberton19')
    wordslist = []
    for i in range(len(x)):
	wordslist.extend(x[i]['text'].encode('utf-8').lower().split())
    return wordslist

def Twitter_checkwords(tweetlist):
    score = 0
    wordlist = []
    for line in tweetlist:
        wordlist = line.split()
        for word in wordlist:
            if word.lower() in gd:
                score += gd[word.lower()]
            elif word.lower() in bd:
		score += bd[word.lower()]
    return score

def Twitter_evaluation(x,user):
    if x > 0:
        return 'User' + user + ' is overall a positive person'
    else:
        return 'User' + user + ' is overall a negative person'

def Twitter_generategoodwordslist():
    cleanlist = []
    aResp = urllib2.urlopen('http://www.creativeaffirmations.com/positive-words.html')
    web_pg = aResp.read()
    pattern1 = '<TD>.*<TD>'
    pattern2 = '[^(<TD>)][A-z][a-z]*[^(<TD>)][^(<TR>)]'
    rslts = re.search(pattern1,web_pg)
    resultslist = rslts.group(0).split('<TD>')
    cleanlist = [word.replace('</TR>','') for word in resultslist]
    cleanlist = [word.replace('<TR>','') for word in cleanlist]
    cleanlist.remove('')
    Twitter_extendgd(cleanlist)
    
def Twitter_generatebadwordslist():
    cleanlist = []
    openfile = open('/Python27/negative-words.txt','r')
    lines = openfile.readlines()
    for i in range(35,4818):
        cleanlist.append(lines[i])
    cleanlist = [word.replace('\n','') for word in cleanlist]
    Twitter_extendbd(cleanlist)

def Twitter_extendgd(goodlist):
    for line in goodlist:
        gd[line] = 1

def Twitter_extendbd(badlist):
    for line in badlist:
        bd[line] = -1

def Twitter_search(topic):
    tweetlist = []
    stream = t.search.tweets(q=topic)
    length = len(stream['statuses'])
    for i in range(len(stream['statuses'])):
        tweetlist.append(stream['statuses'][i]['text'])
    return tweetlist
