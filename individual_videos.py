import requests
import json

def getVideoInformation(version):
  ids = getIds(version)
  lastIndex = len(ids) - 1
  path = "./dump_" + version + "/"

  fo = open(path + "videos.json", 'a')
  fo.write('[')
  for index, item in enumerate(ids):
    vidInfo = getVideoData(item, version)
    fo.write(vidInfo)
    if index != lastIndex:
      fo.write(',')
  fo.write(']')
  fo.close()


# helpers
def getIds(version):
  fo = open("./dump_" + version + "/ids.json", "r")
  ids = json.loads(fo.read())
  fo.close()
  return ids


def getVideoData(id, version):
  url = "https://beeg.com/api/v6/" + version + "/video/" + id
  data = requests.get(url)
  if data.status_code == 200:
    data = data.json()
  else:
    print 'errr'

  return json.dumps({"title": data['title'], "tags": data['tags'], "description": data['desc'], "cast": data['cast'], "producer": data['ps_name']}, sort_keys=True, indent=4, separators=(',', ': '))