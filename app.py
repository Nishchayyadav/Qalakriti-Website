from re import DEBUG
from flask import Flask, render_template
app = Flask(__name__)

Items = []

@app.route("/")
def startSite():
  return render_template('home.html')

@app.route("/login")
def loginPage():
  return render_template('login.html')

@app.route("/register")
def registerPage():
  return render_template('register.html')

@app.route("/cart")
def cartPage():
  return render_template('cart.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug = True)
