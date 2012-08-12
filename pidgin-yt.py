"""
$ python pidgin.py

TODO: It should print the Name of the video in future, not the URL only. Will do when i get time.
"""
import json
from os import system
from time import sleep

#change the below URL with yours
f = open('/home/srikant/.mozilla/firefox/mwad0hks.default/sessionstore.js')
data = json.load(f)
print type(data)
tabs = data['windows'][0]['tabs']

#print tabs
#print [tabs[i]['entries'][-1]['url'] for i in xrange(len(tabs))]
while True:
    sleep(2)
    for i in xrange(len(tabs)):
        a = str(tabs[i]['entries'][-1]['url'])
        print a
        print type(a)
        if "www.youtube" in a:
            system("purple-remote 'setstatus?status=away&message= %s'" %(a))
            print 'ok'
