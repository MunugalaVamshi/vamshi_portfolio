from flask import Flask, render_template, request, redirect, url_for, session
#from werkzeug.security 

app = Flask(__name__)
app.secret_key = "supersecretkey"   # change this in production


# ✅ Home Page
@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
