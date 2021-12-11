import requests
import utils.py
import file_utils.py
import json


def getUserinfo(steamid,authentication_key):
  URL = 'https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/'
  steamids = {'steamids': steamid} 
  key = {'key': authentication_key} 
  res = requests.get(URL, steamids=steamids, key=key)
  return res
  #사용자 정보 획득



def getRecommender(sessionid,steamLoginSecure):
  utils.get_steam_id(steamid)

  json_data['sessionid']= sessionid
  json_data['steamLoginSecure']= steamLoginSecure

  with open('C:\\steam-labs-recommender-master\\personal_info.json', 'w', encoding='utf-8') as make_file:
    json.dump(json_data, make_file, indent="\t")
  with open('C:\\steam-labs-recommender-master\\personal_info.json', 'r') as f:
    json_data = json.load(f)

  exec(open('file_utils.py').read())
  #인터랙티브 추천기 API 사용