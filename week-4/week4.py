from flask import Flask, render_template, session, request, redirect, url_for
import os

app = Flask(__name__, static_folder="static", static_url_path="/")

os.urandom(12)
app.secret_key = '\xc8\x1e\xc1G*D\xb9\xdc;\xbb\xdf\xc2'

users = {"test": ("test", "test")}


@app.route("/")
def home():
	return render_template("home.html")


@app.route("/signin", methods=["POST"])
def signin():
	if request.method == "POST":
		username = request.form.get("username")
		password = request.form.get("password")

		if not username or not password:
			return redirect(url_for("error", message="請輸入帳號、密碼"))

		if username in users and users[username][1] == password:
			session["username"] = username
			return redirect(url_for("member"))
		else:
			return redirect(url_for("error", message="帳號、或密碼輸入錯誤"))


@app.route("/error")
def error():
	err_text = request.args.get("message")
	return render_template("error.html", message=err_text)


@app.route("/member")
def member():
	if session.get("username") is None:
		return redirect(url_for("home"))
	else:
		return render_template("member.html")


@app.route("/signout")
def signout():
	session.pop("username")
	return redirect(url_for("home"))


if __name__ == "__main__":
	app.run(port=3000, debug=True)
