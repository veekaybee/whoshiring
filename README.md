#Who's Hiring on HN?

Hacker News has [links every month](https://news.ycombinator.com/item?id=11012044() where hundreds of companies post looking for candidates. Since the readership is highly technical and  [located in North America and particularly Silicon Valley](https://news.ycombinator.com/item?id=4397332), it's a good proxy of what skills are currently in demand in the industry and 

This script scrapes the link for  Who's Hiring February 2016, strips out the cruft, and compares against Wikipedia's list of computer languages to pull out the relevant terminology. This is counts of mentions in any of the text. So if someone mentioned Java twice in one posting, the program doens't compensate for eagerness.

##Outputs: 

+ Jobs.txt - All scraped and cleaned text
+ Commonjobs.txt - Text compared against Wikipedia list of languages
+ To look at ordered list, run in command line (sorts by second column):
	
	`cat commonjobs.txt | sort -r -k2n `
	

Top 15-ish list:

![image](https://raw.githubusercontent.com/veekaybee/whoshiring/master/top15.png)


## Possible Next Steps: Adventures in Refactoring

* Make the program more modular: split import and export into two different modules so it's not scraping HN every time it's pulled
* Get better at filtering out non-programming related keywords
* Find an API access into HN.. the old Firebase one was deprecated for me
* Sort by other keywords, such as soft skills
* Possibly use NLTK to cluster skills and companies
* Prettier visuals!
* Do a month-month and year-year comparison of growing languages and shrinking languages
* Compare against LinkedIn API's most in-demand languages