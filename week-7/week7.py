from flask import (
    Flask,
    render_template,
    session,
    request,
    redirect,
    url_for,
    jsonify,
)
import bcrypt
from mysql.connector import pooling

app = Flask(__name__, static_folder="static", static_url_path="/")
app.config.from_object("config.Config")

app.secret_key = app.config["SECRET_KEY"]


connection_pool = pooling.MySQLConnectionPool(
    pool_name="mypool",
    pool_size=10,
    user=app.config["USER"],
    password=app.config["PASSWORD"],
    host=app.config["HOST"],
    database=app.config["DATABASE"],
)


class DbConnection:
    def __init__(self):
        self.conn = connection_pool.get_connection()
        self.cursor = self.conn.cursor()

    def execute(self, query, params):
        self.cursor.execute(query, params)

    def commit(self):
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()


def update_member_name(new_name, username):
    update_name = "UPDATE member SET name =%s WHERE username =%s"
    db = DbConnection()
    db.execute(update_name, (new_name, username))
    db.commit()
    affected_row = db.cursor.rowcount
    db.close()
    result = {"error": True}
    if affected_row > 0:
        result = {"ok": True}
    return result


def get_member_info(username):
    select_name = "SELECT id ,name, username FROM member WHERE username =%s"
    db = DbConnection()
    db.execute(select_name, [username])
    result = None
    for id, name, username in db.cursor:
        if username:
            result = {"id": id, "name": name, "username": username}
    db.close()
    return jsonify({"data": result})


def is_username(username):
    select_username = "SELECT member.username FROM member WHERE member.username = %s"
    db = DbConnection()
    db.execute(select_username, [username])
    result = False
    for user in db.cursor:
        if user:
            result = True
    db.close()
    return result


def signup_user(name, username, password):
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    insert_user = "INSERT INTO member (name, username, password) VALUES (%s, %s, %s)"
    db = DbConnection()
    db.execute(insert_user, (name, username, hashed))
    db.commit()
    db.close()


def authenticate_member(username, password):
    select_member = "SELECT name, username, password FROM member WHERE username = %s"
    db = DbConnection()
    db.execute(select_member, [username])
    result = False
    for name, username, hashed in db.cursor:
        if bcrypt.checkpw(password.encode("utf-8"), hashed.encode()):
            result = {"name": name, "username": username}
        else:
            result = False
    db.close()
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
    if is_username(username):
        return redirect(url_for("error", message="帳號已被註冊"))
    else:
        signup_user(name, username, password)
        return redirect(url_for("home"))


@app.route("/signin", methods=["POST"])
def signin():
    username = request.form.get("username")
    password = request.form.get("password")
    if not username or not password:
        return redirect(url_for("error", message="請輸入帳號、密碼"))
    member_name = authenticate_member(username, password)
    if member_name is False:
        return redirect(url_for("error", message="帳號、或密碼輸入錯誤"))
    else:
        session["name"] = member_name["name"]
        session["username"] = member_name["username"]
        return redirect(url_for("member"))


@app.route("/error")
def error():
    err_text = request.args.get("message")
    return render_template("error.html", message=err_text)


@app.route("/member", methods=["POST", "GET"])
def member():
    if request.method == "GET":
        if session.get("name") is None:
            return redirect(url_for("home"))
        else:
            name = session.get("name")
            return render_template("member.html", member=name)


@app.route("/api/members", methods=["GET"])
def get_member():
    username = request.args.get("username")
    member_info = get_member_info(username)
    return member_info


@app.route("/api/member", methods=["POST"])
def update_name():
    username = session.get("username")
    data = request.get_json()
    new_name = data["name"]
    result = update_member_name(new_name, username)
    return jsonify(result)


@app.route("/signout")
def signout():
    session.pop("name")
    session.pop("username")
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(port=3000, debug=True)
