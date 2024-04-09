from re import DEBUG
from flask import Flask, render_template
app = Flask(__name__)

Items = []

@app.route("/")
def startSite():
  return render_template('home.html')
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug = True)
