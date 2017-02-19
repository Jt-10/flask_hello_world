import os
from flask import Flask, render_template
from os import environ

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def hello_world():
    return render_template('template.html',
                  my_string="Hello World!")

@app.route("/kitty/<name>")
def hello_kitty(name):
    html = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a random picture.  Hmmm...
        </p>
        <img src="http://lorempixel.com/400/200">
        """
    return html.format(name.title())


@app.route("/hello/<name>")
def hello_person(name):
    return render_template('template.html',
                  # To remove python string formatting, this needs another template?
                  my_string="Hello {}!".format(name).title())

@app.route("/jedi/<first>/<last>")
def jedi_name(first, last):
    return render_template('template.html',
                  # To remove python string formatting, this needs another template?
                  my_string="Your Jedi name is '{}{}!'".format(last[:3].title(), first[:2]))


if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
