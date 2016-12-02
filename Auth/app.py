#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/auth", methods=["GET", "POST"])
def auth():
    if request.method == "POST":
        secure_id = "test"
        secure_pw = "1234"

        user_id = request.form["id"]
        user_pw = request.form["pw"]

        if secure_id == user_id and secure_pw == user_pw:
            return jsonify(id=user_id, pw=user_pw, status="yes")

        return jsonify(id=user_id, pw=user_pw, status="no")
    return "아이디와 비밀번호를 POST 방식으로 전송해주세요."

@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run()
