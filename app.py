from flask import Flask, render_template,request,flash,session,redirect
#from flask_pymongo import PyMongo

app = Flask(__name__)
#app.config["MONGO_URI"] = ""
#mongo =PyMongo(app)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/signin.html",methods=["GET", "POST"])
def signin():
    if request.method == "POST":
      username = request.form["username"]   #Data Extracted from HTML
      password = request.form["pass"]
      return render_template("idea.html")
    else:
      return render_template("signin.html")


@app.route("/register1.html")
def register():
    return render_template("register1.html")

@app.route("/P1info")
def p1():
    return render_template("p1info.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
