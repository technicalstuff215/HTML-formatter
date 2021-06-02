from flask import Flask, render_template, request, redirect, url_for
from html5print import HTMLBeautifier as hb

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/convert",methods = ["POST"])
def convert():
    raw_html = request.form['incode']
    if(request.form['optionnum'] != "None"):
        indent = request.form['optionnum']
        res = hb.beautify(raw_html,int(indent))
    else:
        return render_template("index.html",code=raw_html, flag=True,sc = True)
    return render_template("index.html", code=res, flag=True)

@app.route("/reset",methods =["POST"])
def reset():
    return redirect("/")
if __name__ == "__main__":
    app.run()
