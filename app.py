import os
import markdown
from flask import Flask, render_template, request
from flask import Markup

app = Flask("__name__")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/tour/<contents_name>")
def contents(contents_name):
    with open('./contents/description/' + contents_name + '.md') as f:
        description = f.read()

    md = markdown.Markdown()
    description = md.convert(description)
    description = Markup(description)

    with open('./contents/code/' + contents_name + ".py") as f:
        code = f.read()

    return render_template("index.html", description=description, code=code)

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)

