import lxml
import requests
from bs4 import BeautifulSoup

#As of 4/10, Creates pages based off ResultsPage links and creates paragraphs and sentances
#TODO: Implement matching
    # If broken check the location of the google garbage at the end of links from h3.[href][x]

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
            if len(i):
                self.sentances.append(i)


class Matches:
    """
        PLAN: Create a Matches object for each webpage
            * structure of self.matches: self.matches[paragraph]-->sentances
                sentances will be the sentances that contain the match for that word
    PASS: A webpage object from the LinksLib library
    
    """
    def __init__(self,WebPage,keywords):
        self.words = keywords
        self.matches = {}
        self.page = WebPage
        
    #_FindPageMatches is probably not needed this version
    def _FindPageMatches(self,webPage):
        "Given a web page object and a list of words, fills self.matches member"
        for para in WebPage.paragraphs:
            self._ParagraphMatches(para)

    def FindMatchesFor(self,keyword):
        "Creates entry in self.matches for the keyword passed"
        #CAUTION: Clears the dictionary before looking for matches
        self.matches[keyword] = []
        for para in self.page.paragraphs:
            for sen in para.sentances:
                if keyword in sentance:
                    self.matches[keyword].append(sen)


    #_FindParagraphMatches is probably not needed this version
    def _ParagraphMatches(self,paragraph):
        "Searches a Paragraph object for sentances that match the keyword"
        self.matches[paragraph] = []
        for sen in paragraph.sentances:
            if (keyword in sen):
                self.matches[paragraph].append(sen)

class WebPage:
    """
        Pass it the http request for the page and it creates an object with
        the 
        METHOD: Matches(self,keyWords)
            * Returns a dictionary of the sentances that contain the keyword passed
                
    """
    def __init__(self,pageRequest):
        self.url = pageRequest.url
        self.bs = BeautifulSoup(pageRequest.text,"lxml")
        self.pTags = self.bs.find_all("p")
        self._CleanPtags()
        self._paragraphs = []
        self._FillParagraphsList()
        self.paragraphs = []
        self._MakeParagraphs()

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
        self._paragraphs = paraList
        
    def _MakeParagraphs(self):
        for para in self._paragraphs:
            self.paragraphs.append(Paragraph(para))
        
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
        self.pages = []
        self.badLinks = []
        self._MakePageObjects()

    def _GetATags(self):
        for tag in self.hTags:
            self.aTags.append(tag.a)
        
        
    def _GenUrls(self):# Fills the Urlsout from 
        # CHECK THIS IF THE LINKS ARE GENERATING 404 RESPONSES, google likes to play games like that
            # May need to use a search to generate the index but it will probably fail if the website uses PHP/Ampersand regex
        googleGibberishStart = -83
        for tag in self.aTags:
            temp = tag['href'][7:] #Urls have a prefix from google searches
            temp = temp[:googleGibberishStart] #Google puts url encoded data after actual link, cuts that off
            self.urls.append(temp) # to prevent always getting 404

    def _MakePageObjects(self):
            i = 0
            for link in self.urls:
                try:
                    c = requests.get(link)
                    self.pages.append(WebPage(c))
                except:
                    i+= 1
                    print(link,"is a bad link!("+str(i)+" total)")
                    self.badLinks.append(link)
                    continue
                
    
def PerformSearch(wordString):
    "Call to perform a search and return a results page based on the passed string."
    #Make sure string is passed with words concatenated with '+' or google will throw a fit
    google = "http://www.google.com/search?"
    searchBase = "&q="
    r = requests.get(google+searchBase+wordString)
    result = ResultsPage(r)
    return result
    
 

