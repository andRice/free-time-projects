import requests as r
from bs4 import BeautifulSoup as bs
import lxml
import LinksLib

sampleSearch = "http://www.google.com/search?&q=test+search"

x = r.get(sampleSearch)

y = bs(x.text,"lxml")

print(str(y.find_by_tag("h3")))

x = LinksLib.PerformSearch("Test+Search")

print(x.urls[2])