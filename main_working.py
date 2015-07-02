#!/usr/bin/env python2.7                                                                                                                              

import feedparser



# deals with where all the feeds come in

# method one
feeda = feedparser.parse('http://krebsonsecurity.com/feed/')
feedb = feedparser.parse('http://www.tripwire.com/state-of-security/feed/')

# method two
# multiple feed test                                                                                                                                  
FEED_List = [
    'http://krebsonsecurity.com/feed/',
    'http://www.tripwire.com/state-of-security/feed/',
    'https://threatpost.com/feed'
    ]

feeds = []
for url in FEED_List:
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

# deals with keywords                                                                                                                                  

keyword = 'hacked'


full_list()

