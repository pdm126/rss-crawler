#!/usr/bin/env python2.7                                                                                                                              

import feedparser

# deals with where all the feeds come in                                                                                                              
feeda = feedparser.parse('http://krebsonsecurity.com/feed/')
feedb = feedparser.parse('http://www.tripwire.com/state-of-security/feed/')

# multiple feed test                                                                                                                                  
FEED_List = [
    'http://krebsonsecurity.com/feed/',
    'http://www.tripwire.com/state-of-security/feed/'
    ]

feeds = []
for url in FEED_List:
    feeds.append(feedparser.parse(url))

for feed in feeds:
    for post in feed.entries:
#        print len(post)                                                                                                                              
        print post.title

# deals with keywords                                                                                                                                  

keyword = 'hacked'

# parses and processes feeds                                                                                                                          

title = feeda['entries'][1].title,
description =  feeda['entries'][1].summary,
url = feeda['entries'][1].link,

posts = []
for i in range(0,len(feeda['entries'])):
    posts.append({
        'title': feeda['entries'][i].title,
        'description': feeda['entries'][i].summary,
        'url': feeda['entries'][i].link,
    })

# searches feeds for keywords                                                                                                                         



# displays results                                                                                                                                    
#print title                                                                                                                                          
#print description                                                                                                                                    
#print url                                                                                                                                            
print 'Feed Details'
print '****'
print 'Available Feeds'
print feeda['feed']['link']
print feedb['feed']['link']
print '****'
print 'Number of Entries'
print len(posts)
print '****'
print 'Most Recent Entries'
print feeda['entries'][0]['title']
print feeda.entries[0]['link']
print feedb['entries'][0]['title']
print feedb.entries[0]['link']
#print feed      
