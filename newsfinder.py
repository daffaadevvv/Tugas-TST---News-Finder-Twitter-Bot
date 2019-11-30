from flask import Flask, jsonify, redirect
import feedparser

app = Flask(__name__)

# Function grabs the rss feed headlines (titles) and returns them as a list
def getHeadlines( rss_url ):
    headlines = []
    
    feed = feedparser.parse( rss_url ) 
    for newsitem in feed['items']:
        headlines.append(newsitem['link'])

    return headlines

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Welcome to News Feeder API</h1>
<p>A prototype API for national and international news feed getter.</p>'''

@app.route('/resources/documentation', methods=['GET'])
def documentation():
    return redirect('https://app.swaggerhub.com/apis/daffaadevvv/NewsFeederAPI/1.0.0', code = 303)


@app.route('/resources/news/internasional', methods=['GET'])
def indexinter():

    # # A list to hold all headlines
    # allinterheadlines = []
    
    # # List of RSS feeds that we will fetch and combine
    # newsinturls = {
    #     # 'rtnews':           'https://www.rt.com/rss/',
    #     'googlenews':       'https://news.google.com/news/rss/?hl=en&amp;ned=us&amp;gl=US'
    # }
    
    # # Iterate over the feed urls
    # for key,url in newsinturls.items():
    #     # Call getHeadlines() and combine the returned headlines with allheadlines
    #     allinterheadlines.extend( getHeadlines( https://news.google.com/news/rss/?hl=en&amp;ned=us&amp;gl=US ) )

    # #print(allinterheadlines)

    # phrase = 'Trump'
    # phrase = phrase.lower()
    # index = 0
    # results = []

    # for interheadline in allinterheadlines:
    #     if phrase in interheadline.lower():
    #         results.append(interheadline)

    # print("lalala")
    # print(results)

    # if re.search(r'\b' + re.escape(phrase) + r'\b', allinterheadlines):
    #     print(index)
    #     

    return jsonify(getHeadlines('https://news.google.com/news/rss/?hl=en&amp;ned=us&amp;gl=US'))


@app.route('/resources/news/dalamnegeri/{keyword}', methods=['GET'])
def indexnat():

    # A list to hold all headlines
    allnatheadlines = []
    
    # List of RSS feeds that we will fetch and combine
    newsnaturls = {
        'republikautama':   'https://www.republika.co.id/rss',
        'bbcindo':          'http://feeds.bbci.co.uk/indonesia/rss.xml',
        'okezone':          'https://sindikasi.okezone.com/index.php/okezone/RSS2.0',
        'detiknews':        'http://rss.detik.com/index.php/detikcom',
        'suara':            'https://www.suara.com/rss',
        'antaranews':       'https://www.antaranews.com/rss/news.xml'
    }
    
    # Iterate over the feed urls
    for key,url in newsnaturls.items():
        # Call getHeadlines() and combine the returned headlines with allheadlines
        allnatheadlines.extend( getHeadlines( url ) )
    
    phrase = 'patimban'
    phrase = phrase.lower()
    index = 0
    results = []

    for natheadline in allnatheadlines:
        if phrase in natheadline.lower():
            results.append(natheadline)
    
    print(results)

    #print(allnatheadlines)

    #return jsonify(allnatheadlines)
    return jsonify(results)


@app.route('/newsfeed/dalamnegeri/<keywords>', methods=['GET'])
def indexn(keywords):
    
    print('data1')
    data = getHeadlines('https://www.republika.co.id/rss')
    print('data2')
    
    phrase = keywords
    phrase = phrase.lower()

    print(phrase)

    for headline in data:
        print(headline)
        if phrase in headline.lower():
            print('data3')
            result = {
                'link': headline
            }
            print(result)
            return jsonify(**result)

    return jsonify('your keywords is not found')

if __name__ == '__main__':
    app.run(debug = True)

