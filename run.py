from flask import Flask, render_template, url_for, flash, redirect, request

app = Flask(__name__)

@app.route("/layout")
def layout():
    return render_template('layout.html')

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/signup")
def signup():
    return render_template('signup_form.html')


@app.route("/portal")
def portal():
    return render_template("portal.html")


@app.route("/expert")
def expert():
    return render_template("expert.html")

@app.route("/dash")
def dashboard():
    return render_template("dash.html")

@app.route("/firm")
def firm():
    return render_template("firm.html")

@app.route("/nonhome")
def nonhome():
    return render_template("non_home_layout.html")


if __name__ == '__main__':
    app.run(debug=True)
