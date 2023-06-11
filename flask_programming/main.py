from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/latinski_pregovori")
def latinski_pregovori():
    return render_template("Latinski pregovori.html")


@app.route("/fake_google")
def fake_google():
    return render_template("Fake Google.html")


@app.route("/bootstrapped_page")
def bootstrapped_page():
    return render_template("Bootstrapped page.html")


if __name__ == '__main__':
    app.run()
