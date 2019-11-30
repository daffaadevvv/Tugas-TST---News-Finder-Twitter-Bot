from flask import Flask, jsonify, redirect
import feedparser
import re

app = Flask(__name__)

# Function grabs the rss feed headlines (titles) and returns them as a list
def getHeadlines( rss_url ):
    headlines = []
    
    feed = feedparser.parse( rss_url ) 
    for newsitem in feed['items']:
        headlines.append(newsitem['link'])

    return headlines

@app.route('/resources/news/dalam/<keyword>', methods=['GET'])
def indexn(keyword):
    
    print('data1')
    data = getHeadlines('https://www.republika.co.id/rss')
    print('data2')
    
    phrase = keyword
    phrase = phrase.lower()
    
    print(phrase)

    result = {
        'phrase': phrase,
        'link': 'Link tidak ditemukan'
    }

    for headline in data:
        print(headline)
        if phrase in headline.lower():
            print('data3')
            result['link'] = headline
            print(result)
            break

    return jsonify(**result)

if __name__ == '__main__':
    app.run(debug = True)

