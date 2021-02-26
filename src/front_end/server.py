from flask import Flask, render_template

# Creates the flask server
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("main_page.html")


@app.route("/code_page")
def code_page():
    return render_template("code_page.html")


@app.route("/free_code")
def free_code():
    return render_template("free_code_page.html")


@app.route("/lessons")
def lessons():
    return render_template("lessons_page.html")


@app.route("/lesson_explained")
def lesson_explained():
    return render_template("lesson_explained.html")


@app.route("/lesson_overview")
def lesson_overview():
    return render_template("lesson_overview.html")


# Starts the flask server
app.run(debug=False, host="0.0.0.0", port=3000)