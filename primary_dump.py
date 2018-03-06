import requests
import json
import os

def dump_main_api(response, version):
  jsonResponse = response.json()
  idArr = []

  for item in jsonResponse['videos']:
    idArr.append(item['id'])

  mainDump = json.dumps(jsonResponse, sort_keys=True, indent=4, separators=(',', ': '))
  idDump = json.dumps(idArr, sort_keys=True, indent=4, separators=(',', ': '))

  files = [["main.json", mainDump], ["ids.json", idDump]]
  path = "./dump_" + version + "/"
  if not os.path.exists(path):
    os.makedirs(path)

  for file in files:
    fo = open(path + file[0], "a")
    fo.write(file[1])
    fo.close