import requests
import json

# get the right number from main file and folder
# track and only print if different

# idArr = []
# titleArr = []
# for item in data['videos']:
#   idArr.append(item['id'])
#   titleArr.append(item['title'])

# mainDump = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
# tagDump = json.dumps(data['tags'], sort_keys=True, indent=4, separators=(',', ': '))
# idDump = json.dumps(idArr, sort_keys=True, indent=4, separators=(',', ': '))
# titleDump = json.dumps(titleArr, sort_keys=True, indent=4, separators=(',', ': '))

# assign to proper folder path
# files = [['beeg{number}.json', mainDump], ['tags{number}.json', tagDump], ['vid_ids{number}.json', idDump], ['titles{number}.json', titleDump]]

# for file in files:
#   fo = open(file[0], "a")
#   fo.write(file[1])
#   fo.close()