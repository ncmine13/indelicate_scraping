import requests
import json
import urllib
import re
import find_bundle_version
import primary_dump
import individual_videos

version = find_bundle_version.getCurrentBundleVersion()
url = "https://beeg.com/api/v6/" + version + "/index/main/0/pc"
data = requests.get(url)

if data.status_code == 200:
  primary_dump.dump_main_api(data, version)
  individual_videos.getVideoInformation(version)
  print 'success!'
else:
  print str(data.status_code)

# next up: improve error message logging, incorporate file paths into imports