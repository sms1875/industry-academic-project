                                        
from flask import Flask, url_for, session, render_template, request, redirect

app = Flask(__name__)
app.secret_key = "qwer1234"

ID = "bank2014"
PW = "qwer1234"

@app.route("/")
def home():
    if "userID" in session:
        return render_template("home.html", username = session.get("userID"), login = True)
    else:
        return render_template("home.html", login = False)

@app.route("/login", methods = ["get"])
def login():
    global ID,PW
    _id_ = request.args.get("loginId")
    _password_ = request.args.get("loginPw")

    if ID == _id_ and _password_ == PW:
        session["userID"] = _id_
        return redirect(url_for("home"))
    else:
        return redirect(url_for("home"))


@app.route("/log out")
def logout():
    session.pop("userID")
    return redirect(url_for("home"))


app.run(host='0.0.0.0')
