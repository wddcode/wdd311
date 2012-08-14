#!/usr/bin/python
# -*- coding: utf-8 -*-
        
import requests

def my_request(id):
    
    url = 'http://api.discogs.com/releases/%s' % id
    
    print 'url: %s' % url
    
    r = requests.get(url)

    for track in r.json['tracklist']:
        d = track['duration']
        t = track['title'] 
        print "%s - %s" % (d, t)
        

my_request('1')



#a, s = my_math(2,4)
#print "a: %s - s: %s" % (a, s)












