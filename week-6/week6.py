from flask import Flask, render_template, session, request, redirect, url_for
import os, bcrypt, mysql.connector

# from mysql.connector import pooling

app = Flask(__name__, static_folder="static", static_url_path="/")

os.urandom(12)
app.secret_key = "\xc8\x1e\xc1G*D\xb9\xdc;\xbb\xdf\xc2"


db = mysql.connector.connect(user="root", password="12345678", host="127.0.0.1", database="website")


def exam_username(db, username):
    select_username = "SELECT member.username FROM member WHERE member.username = %s"
    cursor = db.cursor()
    cursor.execute(select_username, [username])
    result = False
    for user in db.cursor:
        if user:
            result = True
    cursor.close()
    db.close
    return result


def signup_user(db, name, username, password):
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    insert_user = "INSERT INTO member (name, username, password) VALUES (%s, %s, %s)"
    cursor = db.cursor()
    cursor.execute(insert_user, (name, username, hashed))
    db.commit()
    cursor.close()
    db.close


def authenticate_member(db, username, password):
    select_member = "SELECT name, username, password FROM member WHERE username = %s"
    cursor = db.cursor()
    cursor.execute(select_member, [username])
    result = False
    for name, username, hashed in db.cursor:
        if bcrypt.checkpw(password.encode("utf-8"), hashed.encode()):
            result = name
        else:
            result = False
    cursor.close()
    db.close
    return result


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/signup", methods=["POST"])
def signup():
    username = request.form.get("username")
    password = request.form.get("password")
    name = request.form.get("name")
    if not username or not password or not name:
        return redirect(url_for("error", message="請輸入姓名、帳號及密碼"))
    if exam_username(db, username):
        print("username")
        return redirect(url_for("error", message="帳號已被註冊"))
    else:
        signup_user(db, name, username, password)
        return redirect(url_for("home"))


@app.route("/signin", methods=["POST"])
def signin():
    username = request.form.get("username")
    password = request.form.get("password")
    if not username or not password:
        return redirect(url_for("error", message="請輸入帳號、密碼"))
    member_name = authenticate_member(db, username, password)
    if member_name is False:
        return redirect(url_for("error", message="帳號、或密碼輸入錯誤"))
    else:
        session["username"] = member_name
        return redirect(url_for("member"))


@app.route("/error")
def error():
    err_text = request.args.get("message")
    return render_template("error.html", message=err_text)


@app.route("/member")
def member():
    if session.get("username") is None:
        return redirect(url_for("home"))
    else:
        name = session.get("username")
        return render_template("member.html", member=name)


@app.route("/signout")
def signout():
    session.pop("username")
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(port=3000, debug=True)
