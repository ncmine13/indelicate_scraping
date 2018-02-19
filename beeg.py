# just get the correct api and call the other file modules

import requests
import json

from pprint import pprint

# going to need to figure out how they decide on the numbers after v6/
data = requests.get("https://beeg.com/api/v6/2512/index/main/0/pc").json()
# # print data

idArr = []
# titleArr = []
for item in data['videos']:
  idArr.append(item['id'])
#   titleArr.append(item['title'])


# print idArr

# mainDump = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
# tagDump = json.dumps(data['tags'], sort_keys=True, indent=4, separators=(',', ': '))
# idDump = json.dumps(idArr, sort_keys=True, indent=4, separators=(',', ': '))
# titleDump = json.dumps(titleArr, sort_keys=True, indent=4, separators=(',', ': '))

# files = [['beeg3.json', mainDump], ['tags3.json', tagDump], ['vid_ids3.json', idDump], ['titles3.json', titleDump]]
# track and only print if different

# fo = open('./')

# fo = open('./dump_2511/vidInfo2.json', 'a')
numberOfAvailableVideos = len(idArr)

# for file in files:
#   fo = open("./dump_2512/" + file[0], "a")
#   fo.write(file[1])
#   fo.close()

fo = open('./dump_2512/vidInfo3.json', 'a')

def getVideoData(id):
  idStr = "https://beeg.com/api/v6/2512/video/" + id
  data = requests.get(idStr).json()
  dump = json.dumps({"title": data['title'], "tags": data['tags']}, sort_keys=True, indent=4, separators=(',', ': '))
  fo.write(dump)


def constructDumpFile():
  fo.write('[')
  for index, item in enumerate(idArr):
    getVideoData(item)
    if index != numberOfAvailableVideos - 1:
      fo.write(',')
  fo.write(']')
  fo.close()

constructDumpFile()


# one file to figure out what the root of the api is, and two imported sub-modules:
  # one file to grab the titles, tags, and ids, dump only in the appropriate folder
  # after that, one to take the ids and grab all of the individual video tags and titles

