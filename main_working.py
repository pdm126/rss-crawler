#!/usr/bin/env python2.7                                                                                                                              

import feedparser
import sys

# deals with where all the feeds 
feeds = []
Feed_list = []
#f = sys.argv[1]

#with open(f, r) as f:
#    Feed_list = f.readlines()


# multiple feed test                                                                                                                                  
Feed_list = [
    'http://krebsonsecurity.com/feed/',
    'http://www.tripwire.com/state-of-security/feed/',
    'https://threatpost.com/feed'
    ]

for url in Feed_list:
    feeds.append(feedparser.parse(url))



def full_list():
    for feed in feeds:
        for post in feed.entries:
#        print len(post)                                                                                                                              
            print '++++++'
            print post.title
            print post.description
            print post.link
            print '++++++'

def latest_list():
   for feed in feeds:
      for post in feed.entries:
          print post.title
          print ' '
          print post.summary
          print post.link
          print '+++++'
# deals with keywords                                                                                                                                  

keyword = 'hacked'

latest_list()
#full_list()

