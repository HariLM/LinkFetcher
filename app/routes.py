from requests.api import get
from app import app
from flask import render_template, request
from app.lib import getAllLinks

@app.route("/")
def index():
    search_param = request.args.get("search_param")

    data=None
    error=""

    if search_param is not None:
        data,error=getAllLinks(search_param)

    return render_template("index.html", data=data,error=error, search_param=search_param or "")

@app.route("/test")
def test():
    return render_template("test.html")    