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
      return render_template("idea.html")
    else:
      return render_template("signin.html")
    

@app.route("/Register", methods=["GET", "POST"])
def register():
     if request.method == "POST":
      useremail = request.form["email"]   #Data Extracted from HTML
      password = request.form["password"]
      cpassword = request.form["confirming"]
      if (password != cpassword):
         return render_template("register1.html")
      return render_template("idea.html")     
     else:
        return render_template("register1.html")

@app.route("/Idea")
def idea():
    return render_template("idea.html")

@app.route("/P1info")
def p1():
    return render_template("p1info.html")

@app.route("/P2info")
def p2():
    return render_template("p2info.html")

@app.route("/P3info")
def p3():
    return render_template("p3info.html")
    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
