#!/usr/bin/python 

import json
import requests
import urlparse
import fnmatch
import tinyurl
from os import system
from time import sleep
from os import path, walk, system
previousYoutubeURL = ['empty']
matches = []

"""Checking for sessionstore.js, contributed by Sachin Patil"""
for root, dirnames, filenames in walk(path.expanduser('~/.mozilla/firefox/')):
      for filename in fnmatch.filter(filenames, 'sessionstore.js'):
                matches.append(path.join(root, filename))


"""Getting firefox status, sessionstore.js is continuously updated by firefox"""
def readFirefoxTabs():
    f = open(matches[0])
    firefoxData = json.load(f)
    return firefoxData['windows'][0]['tabs']

    
"""This will check for youtube in tabs and retrieve the video name from gdata's URL using JSON"""
def updatePidgin():
    firefoxTabs = readFirefoxTabs()
    for someValue in xrange(len(firefoxTabs)):
        eachURL = str(firefoxTabs[someValue]['entries'][-1]['url'])
        if "www.youtube.com" in eachURL and eachURL != previousYoutubeURL[0]:
            url_data = urlparse.urlparse(eachURL)             
            query = urlparse.parse_qs(url_data.query)
            response = requests.get("http://gdata.youtube.com/feeds/api/videos/%s?v=2&alt=jsonc" %(query["v"][0]))
            if(response.status_code == 200):                                                               
                video_id = json.loads(response.content)
                system("purple-remote 'setstatus?status=online&message=is watching: %s on youtube[%s]'"\
                %(video_id['data']['title'],tinyurl.create_one(eachURL)))
                previousYoutubeURL[0] = eachURL



if __name__=="__main__":
    while True:
        updatePidgin()
        sleep(2)
