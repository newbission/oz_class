from flask import Flask, render_template, redirect, url_for
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

# 사용자 정보
users = {"admin": "secret", "guest": "guest"}


@auth.verify_password
def verify_password(username, password):
    if username in users and users[username] == password:
        return username


@app.route("/protected")
@auth.login_required
def protected():
    return render_template("secret.html")


@app.route("/")
def index():
    return render_template("index.html")


@auth.error_handler
def auth_error(status):
    return "Access Denied", status


if __name__ == "__main__":
    app.run(debug=True)
