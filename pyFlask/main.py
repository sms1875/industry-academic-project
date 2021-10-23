from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return '산학프로젝트  <h1> 스팀게임 추천 서비스 웹페이지입니다. </h>'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port = 5000)