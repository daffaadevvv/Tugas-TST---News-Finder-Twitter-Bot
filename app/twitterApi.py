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

def mentionID(mention = mentionCheck()):
    print (mention[0].user.id)
    return mention[0].user.id

def mentionUser(mention = mentionCheck()):
    print(mention[0].user.screen_name)
    return mention[0].user.screen_name

def mentionMessage(mention = mentionCheck()):
    message_string = mention[0].text.split( )
    query = mentionRemove(message_string)
    return query[0]

def postTweet(link):
    print(link)
    
    text = '@' + mentionUser() + ' ' + link

    api.PostUpdate(status=text, in_reply_to_status_id=mentionID())
    
    return text

def callNews(result = mentionMessage()):
    req_link = requests.get('http://127.0.0.1:5000/news/dalam/' + result).json()
    
    link = req_link['link']
    
    tweetMessage = postTweet(link)

    jsonResponse = {
        'code': 200,
        'message': 'request success',
        'data': tweetMessage,
        'to reply query': mentionMessage(),
        'in reply to': mentionUser(),
        'with ID': mentionID()
    }
    
    return jsonResponse


# DEBUG FUNCTION

def jsonMessage(mention = mentionCheck()):
    message_string = mention[0].text.split( )

    jsonResponse = {
        'code': 200,
        'message': 'request success',
        'data': mentionRemove(message_string)[0]
    }
    
    return jsonResponse

def jsonUser(mention = mentionCheck()):
    jsonResponse = {
        'code': 200,
        'message': 'request success',
        'data': (mention[0].user.screen_name)
    }
    return jsonResponse

def jsonTweet():
    api.PostUpdates('BotTwitter Tes')
    
    jsonResponse = {
        'data': 'sukses gan'
    }

    return jsonResponse

def jsonID(mention = mentionCheck()):
    jsonResponse = {
        'code': 200,
        'message': 'request success',
        'data': mention[0].user.id
    }
    return jsonResponse