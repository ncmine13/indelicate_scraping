import requests
import json
import urllib
import re
from bs4 import BeautifulSoup

try:
 import BeautifulSoup
except ImportError, e:
 pass # module doesn't exist, deal with it.

web = urllib.urlopen("https://beeg.com/")
soup = BeautifulSoup(web.read(), 'lxml')
# data  = soup.find("script").string

print soup.prettify()