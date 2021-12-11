from utils import get_session_id




session = requests.Session()
data = {'username': "myUserName", 'password': "myPassWord"}
request = session.post("https://steamcommunity.com/login/", data=data)
print(request.cookies)
