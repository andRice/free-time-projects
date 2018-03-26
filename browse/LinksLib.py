import lxml
import requests
from bs4 import BeautifulSoup

#As of 3/21, ResultsPage succesfully generates list of urls that generate valid (200) responses
    # If broken check the location of the google garbage at the end of links from h3.1[href][x]

#**********HIGH LEVEL OVERVIEW*****************
#   -Create request for google seach page with correct query
#       *Store these results in a ResultsPage object for iteration
#   -Create Page object from each link (WebPage object)
#       * Store WebPage objects in results page

class Paragraph:
    "Generated from p-tags, have a breakdown of their sentances for easier indexing"

    def __init__(self,words):
        "Takes in a string and splits by period to generate sentances"
        self.words = words
        self.sentances = []
        self._MakeSentances()
            
    def _MakeSentances(self):
        for i in self.words.split("."):
            self.sentances.append(i)

class WebPage:
    """
        Pass it the http request for the page and it creates an object with
        the 
        METHOD: Matches(self,keyWords)
            * Returns a dictionary of the sentances that contain the keyword passed
                * Dict format[paragraph(int)]:"Sentance"(string)
    """
    def __init__(self,pageRequest):
        self.bs = BeautifulSoup(pageRequest.text,"lxml")
        self.pTags = self.bs.find_all("p")
        self._CleanPtags()
        self.paragraphs = []
        self._FillParagraphsList()
        
    def _CleanPtags(self):
    #Makes sure all the tags have information in them
        newList = []
        for tag in self.pTags:
            if (len(tag.text) >= 5):#5 is the minimum number of words for a tag to be considered "good"
                newList.append(tag)
        self.pTags = newList
        
    def _FillParagraphsList(self):
        paraList = []
        for tag in self.pTags:
            paraList.append(tag.text)
        self.paragraphs = paraList
        
        
        
class ResultsPage:
    def __init__(self,request):
        self.bs = BeautifulSoup(request.text,"lxml")
        self.hTags = self.bs.find_all("h3")
        self.aTags = []
        self._GetATags()
        self.pages = []
        #Access the actual link in a tag by doing a['href']
        self.urls = []
        self._GenUrls()
        
        
    def _GetATags(self):
        for tag in self.hTags:
            self.aTags.append(tag.a)
        
        
    def _GenUrls(self):# Fills the Urlsout from 
        # CHECK THIS IF THE LINKS ARE GENERATING 404 RESPONSES, google likes to play games like that
            # May need to use a search to generate the index but it will probably fail if the website uses PHP/Ampersand regex
        googleBullshitStart = -83
        for tag in self.aTags:
            temp = tag['href'][7:] #Urls have a prefix from google searches
            temp = temp[:googleBullshitStart] #Google puts url encoded data after actual link, cuts that off
            self.urls.append(temp) # to prevent always getting 404
    
    
def PerformSearch(wordString):
    
    google = "http://www.google.com/search?"
    searchBase = "&q="
    r = requests.get(google+searchBase+wordString)
    result = ResultsPage(r)
    return result
    
    