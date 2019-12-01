from flask import Flask, Response, redirect, request, jsonify
import json
import twitterApi
import newsFinder

app = Flask(__name__)
app.config['DEBUG'] = True

def response_api(data):
    return jsonify(**data)

@app.route('/twitter/mention', methods=['GET'])
def mention():
    try:
        data = twitterApi.callNews()
        return response_api(data)
    except Exception as e:
        return e

@app.route('/news/dalam/<keyword>', methods=['GET'])
def news(keyword):
    try:
        data = newsFinder.dalamNegeri(keyword)
        return response_api(data)
    except Exception as e:
        return e


# DEBUG ENDPOINT

@app.route('/twitter/mention/message', methods=['GET'])
def message():
    try:
        data = twitterApi.jsonMessage()
        return response_api(data)
    except Exception as e:
        return e

@app.route('/twitter/mention/user', methods=['GET'])
def user():
    try:
        data = twitterApi.jsonUser()
        return response_api(data)
    except Exception as e:
        return e

@app.route('/twitter/mention/id', methods=['GET'])
def id():
    try:
        data = twitterApi.jsonID()
        return response_api(data)
    except Exception as e:
        return e

@app.route('/twitter/post', methods=['GET'])
def update():
    try:
        data = twitterApi.jsonTweet()
        return response_api(data)
    except Exception as e:
        return response_api(e)

if __name__ == "__main__":
    app.run()