import LinksLib as ll
import config

want = config.keyterms
searchWords = config.searchterms
outputFile = config.writeto


#___________CREATE RESULTSPAGE OBJECTS____________
resultPages = []
for thing in want:
    resultPages.append(ll.PerformSearch(thing))
#=================================================

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
        _FindPageMatches(WebPage)
        #self.pages =  # List of all the results pages

    def _FindPageMatches(self,webPage):
        "Given a web page object and a list of words, fills self.matches member"
        for para in WebPage.paragraphs:
            self._ParagraphMatches(para)


    def _ParagraphMatches(self,paragraph):
        "Searches a Paragraph object for sentances that match the keyword"
        self.matches[paragraph] = []
        for sen in paragraph.sentances:
            if (keyword in sen):
                self.matches[paragraph].append(sen)


