import urllib
import urllib2
import json

urlToRequest = "http://api.wunderground.com/api/236a084f2593c51c/conditions/q/CA/94115.json"

request = urllib2.Request(urlToRequest)
response = urllib2.urlopen(request)

jsonData = json.load(response)

print jsonData["current_observation"]["temp_f"]
