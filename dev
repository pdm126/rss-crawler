#!/usr/bin/env python2.7                                                                                                                              

import feedparser
import sys

# holds the feeds

feeds = []
Feed_list = []
kill = 'g'

# multiple feed list                                                                                                                                 
Feed_list = [
'http://krebsonsecurity.com/feed/',
'http://www.tripwire.com/state-of-security/feed/',
'https://threatpost.com/feed'
	]

# appends list of feeds via feed parser into big list, slow to load in
for url in Feed_list:
		feeds.append(feedparser.parse(url))
    	

def full_list():
	# option e feed by chunk
    for feed in feeds:
        for post in feed.entries:                                                                                                                            
            print '++++++'
            print post.title
            print post.description
            print post.link
            print '++++++'
        kill == raw_input('next? ')
        if kill == 'y':
          		menu()

def latest_list():
	# option d - line by line*
   for feed in feeds:
      for post in feed.entries:
          print post.title
          print ' '
          print post.summary
          print post.link
          print '+++++'
          kill == raw_input('next? ')
          if kill == 'y':
          	menu()
          
def quick_list():
	# option c line by line
   for feed in feeds:
      for post in feed.entries:
          print post.title
          print post.link
          print '+++++'
          kill == raw_input('next? ')
          if kill == 'y':
          	menu()
    
# deals with keywords                                                                                                                                  

def keyword_title(term):
	for feed in feeds:
		for post in feed.entries:
			if term in post.title:
				print 'found keyword ' + term + ' on '
				print post.title + '/n' + post.link
				again1()
				if term not in post.summary:
					print 'not found'
					again1()

def keyword_full(term):
	for feed in feeds:
		for post in feed.entries:
			if term in post.summary:
				print 'found keyword ' + term + ' on ' + post.link
				again()
				if term not in post.summary:
					print 'not found'
					again()
			
def	again(): 
	go_again = raw_input('again? ')
	if go_again == 'y':
		term = raw_input('Search term? ')
		keyword_full(term)
	if go_again == 'n':
		menu()
			

def	again1(): 
	go_again1 = raw_input('again? ')
	if go_again1 == 'y':
		term = raw_input('Search term? ')
		keyword_title(term)
	if go_again1 == 'n':
		menu()
		
def menu():
	print 'Welcome Dr Falken'
	print ' '
	print 'a) Deep RSS Keyword Search'
	print 'b) RSS title search'
	print 'c) Top post of feeds'
	print 'd) Summary List of Feeds'
	print 'e) Full list of feeds'
	choice = raw_input('please choose an option ')
	print 'chosen ' + choice + ' good choice. '
	if choice == 'a':
		term = raw_input('Search term ?')
		keyword_full(term)
	if choice == 'b':
		term = raw_input('Search term ?')
		keyword_title(term)
	if choice == 'c':
		quick_list()
	if choice == 'd':
		latest_list()
	if choice == 'e':
		full_list() 

menu()
