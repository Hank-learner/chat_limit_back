#!/usr/bin/env python3
from flask import Flask, request
import logging
from flask_mysqldb import MySQL
from sentiment import sentiment
import sys
from flask_cors import CORS

# from auth import authentication
app = Flask(__name__)
app.debug = True
CORS(app)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "tonyjones"
app.config["MYSQL_DB"] = "chat"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
# mysql initialization
mysql = MySQL(app)


@app.route("/")
def index():
    return "hello from flask";


@app.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        usernamegot = request.form["user"]
        passwordgot = request.form["pass"]

        output = "failure"

        cursor = mysql.connection.cursor()
        result = cursor.execute(
            "SELECT  * from users where name='{0}'".format(usernamegot)
        )

        if result > 0:
            data = cursor.fetchone()
            password = data["password"]
            password = str(password)

            if password == passwordgot:
                output = "success"

        return {"message": output}
    else:
        return "You are not supposed to be here: You have registered to be hacked by your activity"

@app.route("/sentiment",methods=["POST"])
def sentiment():
    if request.method == "POST":
        messagegot = request.form["message"]
        mood = sentiment(message)
        return mood

if __name__ == "___main__":
    app.secret_key = "secret123"
    app.run(debug=True,host= '0.0.0.0',port=1235)
