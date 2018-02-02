# just get the correct api and call the other file modules

import requests
import json

from pprint import pprint

# going to need to figure out how they decide on the numbers after v6/
data = requests.get("https://beeg.com/api/v6/2511/index/main/0/pc").json()
# print data

idArr = []
titleArr = []
for item in data['videos']:
  idArr.append(item['id'])
  titleArr.append(item['title'])

mainDump = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
tagDump = json.dumps(data['tags'], sort_keys=True, indent=4, separators=(',', ': '))
idDump = json.dumps(idArr, sort_keys=True, indent=4, separators=(',', ': '))
titleDump = json.dumps(titleArr, sort_keys=True, indent=4, separators=(',', ': '))

# for /v6/2509
# files = [['beeg.json', mainDump], ['tags.json', tagDump], ['vid_ids.json', idDump], ['titles.json', titleDump]]
# for /v6/2511
files = [['beeg2.json', mainDump], ['tags2.json', tagDump], ['vid_ids2.json', idDump], ['titles2.json', titleDump]]
# track and only print if different

def getVideoData(id):
  idStr = "https://beeg.com/api/v6/2511/video/" + id
  data = requests.get(idStr).json()
  dump = json.dumps({"title": data['title'], "tags": data['tags']}, sort_keys=True, indent=4, separators=(',', ': '))
  fo = open('vidInfo2.json', 'a')
  fo.write(dump)
  fo.close()

# getVideoData(idArr[0])
# for item in idArr:
#   getVideoData(item)

# for file in files:
#   fo = open(file[0], "a")
#   fo.write(file[1])
#   fo.close()



# one file to figure out what the root of the api is, and two imported sub-modules:
  # one file to grab the titles, tags, and ids, dump only in the appropriate folder
  # after that, one to take the ids and grab all of the individual video tags and titles

