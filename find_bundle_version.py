import urllib
import re
from bs4 import BeautifulSoup

web = urllib.urlopen("https://beeg.com/")
soup = BeautifulSoup(web.read(), 'lxml')
data  = soup.find_all("script")
length = len(data)
current_bundle_version = data[length - 1]['src']

num = re.split(r'[`\-_+\[\]\'\\./]', current_bundle_version)
i = 0

while i < len(num):
  if (num[i].isdigit()):
    current_bundle_version = int(num[i])
    break
  i+=1

print current_bundle_version