import feedparser

# Function grabs the rss feed headlines (titles) and returns them as a list
def getHeadlines( rss_url ):
    listLink = []
    
    feed = feedparser.parse( rss_url ) 
    for newsitem in feed['items']:
        listLink.append(newsitem['link'])

    return listLink

def dalamNegeri(keyword):
    listLink = getHeadlines('https://www.republika.co.id/rss')
    
    phrase = keyword.lower()
    
    result = {
        'phrase': phrase,
        'link': 'Link tidak ditemukan'
    }

    for link in listLink:
        if phrase in link.lower():
            result['link'] = link
            break

    return result

