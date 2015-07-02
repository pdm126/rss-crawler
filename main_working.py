#!/usr/bin/env python2.7                                                                                                                              

import feedparser

# deals with where all the feeds come in                                                                                                              
#feed = feedparser.parse('http://www.reddit.com/r/python/.rss')                                                                                       
#feed = feedparser.parse('http://feeds.bbci.co.uk/news/scotland/rss.xml?edition=uk')                                                                  

# multiple feed test                                                                                                                                  
FEED_List = [
    'http://feeds.bbci.co.uk/news/scotland/rss.xml?edition=uk',
    'http://www.gameinformer.com/b/MainFeed.aspx?Tags=preview',
    ]

feeds = []
for url in FEED_List:
    feeds.append(feedparser.parse(url))

for feed in feeds:
    for post in feed.entries:
        print len(post)
        print feed.title
        
# deals with kewords                                                                                                                                  

keyword = 'hacked'

# parses and processes feeds                                                                                                                          

title = feed['entries'][1].title,
description =  feed['entries'][1].summary,
url = feed['entries'][1].link,
posts = []
for i in range(0,len(feed['entries'])):
    posts.append({
        'title': feed['entries'][i].title,
        'description': feed['entries'][i].summary,
        'url': feed['entries'][i].link,
    })

# searches feeds for keywords                                                                                                                         



# displays results                                                                                                                                    
print title
print description
print url
print 'Feed Details'
print '****'
print 'Available Feeds'
print feed['feed']['link']
print '****'
print 'Number of Entries'
print len(posts)
print 'Most Recent Entry'
print feed['entries'][0]['title']
print feed.entries[0]['link']
print feed

