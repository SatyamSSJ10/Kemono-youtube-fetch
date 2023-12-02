import re
import os
import json
import ast
import requests as req

BASE_URL = r"https://kemono.party"
API = r"api/v1"
SERVICE_URL = "patreon"
CREATOR_ID = 111111
OFFSET = 0
POST_LIST = []

def fetch_posts(OFFSET = 0):
    res = req.get(str('/'.join([BASE_URL,API,SERVICE_URL,"user",CREATOR_ID,"?o="]))+ str(OFFSET), headers={'accept': r'application/json'})
    return json.loads(res.text)

def find_links(obj):
    res = re.compile(r'(?:https?:\/\/)?(?:www\.)?(?:youtu\.be\/|youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=))([^"&?\/\s]{11})')
    res = res.findall(obj)
    return res

def make_list(obj):
    if (n:=len(obj['attachments'])) == 0:
        attachment = ''
    else:
        attachment = [BASE_URL + "/" + str(s['path']) for s in obj['attachments']]
        #attachment = [BASE_URL+"/"+str(obj['attachments'][s]['path'] for s in range(n))]
        #str(obj['path']) for obj in attachment.get("attachments", [])
    if len(m:=find_links(obj['content']))!=0:
        vid_id = m[0]
    else:
        return [obj['title'],attachment]
    return [obj['title'],attachment,r"https://youtu.be/" + vid_id]

def save_list_local(content = None):
    with open(str(OFFSET)+".txt","a",encoding="utf-8") as f:
        for i in range(len(content)):
            f.write(str(content[i]) +"\n")

while 1:
    res = fetch_posts(OFFSET)
    try:
      if len(res) == 0:
          break
    except:
        continue
    for i in range(len(res)):
      POST_LIST.append(make_list(res[i]))
    save_list_local(POST_LIST)
    OFFSET = OFFSET + 50
