from flask import Flask
import json
import twitter
import requests

CONSUMER_KEY = 'NtSd91Sg1FTL89OWWG8AKZtbb'
CONSUMER_SECRET = 'vNO3U5p8LwYd5yLzNobM7Pv9pND58mUyRZMmSszq982OT5llTu'
ACCESS_TOKEN = '216299873-JxwWo6jF0CYw2ZSVjGWjumiIrQzl9UVlq3ykhtmy'
ACCESS_SECRET = 'Im00D6v4rw75JC3uY1YNOgy5XCBaLwvwDMnKRdQ0o74zz'

app = Flask(__name__)
app.config['DEBUG'] = True

api = twitter.Api(consumer_key=CONSUMER_KEY,
            consumer_secret=CONSUMER_SECRET,
            access_token_key=ACCESS_TOKEN,
            access_token_secret=ACCESS_SECRET)

# Delete word with @ in the beginning
def cekString(string):
    if string[0] != '@' :
        return True

# Give a new message to another API
def mentionRemove(array):
    message_fix = []
    
    for item in array:
        if cekString(item):
            message_fix.append(item)
    
    return message_fix

def mentionCheck():
    mention = api.GetMentions(count=1)

    return mention

def mentionUser(mention = mentionCheck()):
    return mention[0].user.screen_name

def mentionMessage(mention = mentionCheck()):
    message_string = mention[0].text.split( )

    return mentionRemove(message_string)

def postTweet(link, username = mentionUser()):
    print(link)
    text = '@' + username + ' ' + link
    print(text)
    api.PostUpdate(status=text)
    print('sampe sini gan')
    return text

def callNews(result = mentionMessage()):
    req_link = requests.get('http://127.0.0.1:5000/news/dalam/' + result).json()
    
    link = req_link['link']
    
    tweetMessage = postTweet(link)

    jsonResponse = {
        'code': 200,
        'message': 'request success',
        'data': tweetMessage
    }
    
    return jsonResponse