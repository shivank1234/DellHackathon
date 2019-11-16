from flask import Flask, render_template,request,flash,session,redirect  

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
    
@app.route("/SignIn",methods=["GET", "POST"])
def signin():
    if request.method == "POST":
      username = request.form["username"]   #Data Extracted from HTML
      password = request.form["pass"]
    else:
      return render_template("signin.html")
    return 'OK'

@app.route("/Register")
def register():
    return render_template("register.html")

@app.route("/P1info")
def p1():
    return render_template("p1info.html")
    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
