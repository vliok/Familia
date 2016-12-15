import urllib2, json, os, urllib, datetime, keys

key = keys.get_key("TMDB")

def get_popmovies():
    url = "https://api.themoviedb.org/3/movie/now_playing?api_key=" + key + "&language=en-US&page=1"
    request = urllib2.urlopen(url)
    result = request.read()
    d = json.loads(result)
    retList = []
    for movie in d["results"]:
        retList.append( movie["original_title"] )
    return retList

#print get_popmovies()
