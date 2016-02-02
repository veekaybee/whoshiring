# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import re
import wikipedia

#Script gets most commonly asked for programming languages by mentions from HackerNews

#Scrape HackerNews Who's Hiring February 2016 Page 

address = "https://news.ycombinator.com/item?id=11012044"

response = urllib2.urlopen(address)
soup = BeautifulSoup(response,"lxml")
tag = soup.find_all('span', 'c00')


with open('jobs.txt', 'w') as jobs:
 	for line in tag:
 		jobs.write(str(line))

#write scraped output to file and clean-up
#wordcount produces individual words and frequency of appearance in webpage
with open('jobs.txt', 'r') as jobsr:
	wordcount={}
	for line in jobsr:
		URLless_string = re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''', '', line)
		nohtml = re.sub('<[^<]+?>', '', URLless_string)
		words = re.split('\W+', nohtml)
		for word in words: 
			word = word.lower()
			if word not in wordcount:
		   		wordcount[word] = 1
			else: 
				wordcount[word] += 1

	

#clean up list of frequent word to limit to only programming languages by polling Wikipedia

wk = wikipedia.page("List of programming languages")
links = wk.links

language_list  = []

for i in links:	
	splitlinks = re.split('\W+',i)
	language = re.findall(r"\w+", i)
	languages =  language[0].lower()
	language_list.append(languages)

#spits out list of programming languages to textfile
#order by cat commonjobs.txt | sort -r -k2n 

common_language = {k: wordcount[k] for k in language_list if k in wordcount}

with open('commonjobs.txt', 'w') as jobdict:
		for k,v in common_language.iteritems():
			jobdict.write(k + " " + ","  + str(v) + "\n")


