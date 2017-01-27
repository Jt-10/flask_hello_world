import os
from flask import Flask
from os import environ

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
    return "Hello World!"

@app.route("/hello/<name>")
def hello_person(name):
    html = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a picture of a kitten.  Awww...
        </p>
        <img src="http://placekitten.com/g/200/300">
    """
    return html.format(name.title())

@app.route("/jedi/<first>/<last>")
def jedi_name(first, last):
    return "Your Jedi name is '{}{}!'".format(last[:3].title(), first[:2])

if __name__=="__main__":
    app.run(host=os.environ.get('IP', ''),
            port=os.environ.get('PORT', 8080))
