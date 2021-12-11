from utils import get_session_id





session = requests.Session()


def getAppList():
  request = session.post("https://api.steampowered.com/ISteamApps/GetAppList/v2")
  return request