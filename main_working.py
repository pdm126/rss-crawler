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

titleb = feedb['entries'][1].title,
descriptionb = feedb['entries'][1].summary,
urlb = feeda['entries'][1].link,

postsb = []
    for i in range(0,len(feedb['entries'])):
    posts.append({
        'title': feedb['entries'][i].title,
        'description': feedb['entries'][i].summary,
        'url': feedb['entries'][i].link,
})

# searches feeds for keywords                                                                                                                         



# displays results                                                                                                                                    
                                                                                                                                            
print 'Feed Details'
print '****'
print 'Available Feeds'
print feeda['feed']['link']
print 'Number of Entries'
print len(posts)
print title                                                                                                                                          
print description                                                                                                                                    
print url
print '****'
print feedb['feed']['link']
print 'Number of Entries'
print len(postsb)
print titleb                                                                                                                                          
print descriptionb                                                                                                                                    
print urlb
print '****'

print '****'
print 'Most Recent Entries'
print feeda['entries'][0]['title']
print feeda.entries[0]['link']
print feedb['entries'][0]['title']
print feedb.entries[0]['link']
#print feed  
