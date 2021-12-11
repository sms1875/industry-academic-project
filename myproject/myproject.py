                                        
from flask import Flask, url_for, session, render_template, request, redirect

app = Flask(__name__)
app.secret_key = "qwer1234"


@app.route("/")
def home():
    if "userID" in session:
        return render_template("home.html", username = session.get("userID"), login = True)
    else:
        return render_template("home.html", login = False)

@app.route("/login", methods = ["get"])
def login():
    pass

@app.route("/log out")
def logout():
    pass


app.run(host='0.0.0.0')
