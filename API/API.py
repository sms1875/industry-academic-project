import requests


def getUserinfo():
  URL = 'https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/'

  steamids = {'steamids': 'steamids'} 
  key = {'key': 'authentication key'} 
  res = requests.get(URL, steamids=steamids, key=key)
  return res
  #»ç¿ëÀÚ Á¤º¸ È¹µæ