from splinter import Browser
import time
import lxml
import requests
from bs4 import BeautifulSoup
import config
import os


google = "http://www.google.com/search?"
searchBase = "&q="
scanner_list = config.keyterms + config.searchterms # For scanning links to click

# find_by_tag(self, tag) Finds an element by its tag
	# Use with HTML p tags to split at paragraphs on links to find info with specific keywords from config
	
#search_click = b.find_by_name("btnG")  # Button to click to perform the search, from google source code

#wfile = open(config.writeto, "a") # Opens the file in the directory for dumping, append mode so it doesn't overwrite
#b = Browser("chrome")  # Opens Browser to chrome, sends to google.com to search the terms in the config file, currently stilyagi-based
#b.visit("https:\\google.com")
#xxx = len(config.searchterms)

#       NEED FROM SEARCH PAGE
#1. List of all the <p> tags
#2. Shorten list to exclude extremely small paragraphs

#**FROM RESULTS PAGE, KEEP TRACK OF ALL THE HREFs***********
#class ResultsPage:
#    def __init__(self,request):
#        self.bs = BeautifulSoup(request.text,"lxml")
#        self.hTags = self.bs.find_by_tag("h3")
#        self.aTags = self.hTags.a
#        #Access the actual link in a tag by doing a['href']
#        self.Urls = []
#        self._GenPages(self)
#        
#    def _GenPages(self):# Fills the Urlsout from 
#        for tag in self.aTags:
#            self.Urls.append(tag['href'])

            
#class Website:
#    def __init__(self,request):
        
            
#       NEED FROM EACH PAGE
#1. Enumerated list of paragraphs
#2. Dictionary with paragraph index mapped to list of sentences
#3. Dictionary with paragraph index mapped to list of matching sentences
#
#

def ResultsHrefs(page):
    "After navigating to the results page, call this to generate the list of links to 'click'"
    linkList = []
    newPage = ResultsPage(page)
    linksList = newPage.Urls
    
    
def GrabLinks():
    "Grabs all the links from searching based on the config file"
    searchLinks = {}
    for search in config.searchterms:
        query = searchBase + search
        searchPage = requests.get(google+query)
        links = ResultsHrefs(searchPage)
        searchLinks[search] = links # I guess that's why it's called searchLinks
    return searchLinks
    
    
def NewSearch(): # Uses exclusively requests and the REST API
    "Basically just main"
    #searchLinks is a dictionary of [search term]:List of links generated from that google search
    searchLinks = {}
    for search in config.searchterms:
        query = searchBase + search
        searchPage = requests.get(google+query)
        links = ResultsHrefs(searchPage)
        searchLinks[search] = links # I guess that's why it's called searchLinks
    
        #for i in range(len(links)):
        #    searchLinks[i] = ResultsHrefs()



#try:

#def OldSearch():# With the browser being physically run
#    for i in range(x):
#        b.fill("q", config.searchterms[i])
#        search_click.click()
#        list_of_links = b.find_by_tag("h3")
#        for link in list_of_links:
#            wfile.write(b.url, "\n")
#            text_block = ""
#            link.click()
#            cc = b.find_by_tag("p") # finds all the <p> tags in the HTML
#            for p in cc:
#                #for x in range())
#                    if len(p.text) > 0:
#                        text_block += p.text
#            s_list = text_block.split(".")  # Now the text block is a list of sentences
#            for sentence in s_list:
#                for word in config.keyterms:
#                    if word in sentence:
#                        wfile.write(sentence, "\n")
#        b.back()

#except:
	#pass

	# TODO Make it click on each link that matches the query and then
	# break the text from the website into sentances based on the the
	# Keyterms.  Then write the sentances that fit the query into the file