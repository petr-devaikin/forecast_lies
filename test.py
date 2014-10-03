import urllib2, urllib, json
baseurl = "https://query.yahooapis.com/v1/public/yql?"
yql_query = 'select item from weather.forecast ' + \
    ' where woeid in (select woeid from geo.places(1) where text="moscow") and u="c"'
yql_url = baseurl + urllib.urlencode({'q':yql_query}) + "&format=json"
result = urllib2.urlopen(yql_url).read()
data = json.loads(result)
print data['query']['results']['channel']['item']['forecast']