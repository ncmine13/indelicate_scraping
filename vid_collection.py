import requests
import json

# receive proper folder number
# import id file info from appropriate folder
# idArr = info

# def getVideoData(id):
#   idStr = "https://beeg.com/api/v6/{number}/video/" + id
#   data = requests.get(idStr).json()
#   dump = json.dumps({"title": data['title'], "tags": data['tags']}, sort_keys=True, indent=4, separators=(',', ': '))
#   fo = open('vidInfo{number}.json', 'a')
#   fo.write(dump)
#   fo.close()

# for item in idArr:
#   getVideoData(item)