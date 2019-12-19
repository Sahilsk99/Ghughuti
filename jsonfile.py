import urllib.request
import json

def response(url):
    with urllib.request.urlopen(url) as response:
        return response.read()
resp = response("http://garhkumo.com/Api/channel")
channel_data = json.loads(resp)
print(channel_data,len(channel_data))
### Method 1

import requests
r = requests.get(url='https://garhkumo.com/technowebtech/api/index.php?url=channel')
print(r.json())


### Method 2

import requests
import json
url = 'https://garhkumo.com/technowebtech/api/index.php?url=channel'
r = requests.get(url)
print(json.loads(r.content))


## Method 3

import urllib.request
import json
url = 'https://garhkumo.com/technowebtech/api/index.php?url=channel'
def response(url):
    with urllib.request.urlopen(url) as response:
        return response.read()
res = response(url)
print(json.loads(res))
