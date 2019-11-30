from flask import Flask, Response, redirect, request, jsonify
import json
import twitter

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
    response = {
        'code': 200,
        'message': 'Request Success',
        'data' : mention[0].user.screen_name
    }

    return response

def mentionMessage(mention = mentionCheck()):
    message_string = mention[0].text.split( )
    response = {
        'code': 200,
        'message': 'Request Success',
        'data' : (' '.join(mentionRemove(message_string)))
    }

    return response

def response_api(data):
    return jsonify(**data)

@app.route('/twitter/mention/message', methods=['GET'])
def message():
    try:
        data = mentionMessage()
        return response_api(data)
    except Exception as e:
        return e

@app.route('/twitter/mention/user', methods=['GET'])
def user():
    try:
        data = mentionUser()
        print(data)
        return response_api(data)
    except Exception as e:
        return e


if __name__ == "__main__":
    app.run()