from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("main_page.html")

@app.route('/code_page')
def code_page():
    return render_template("code_page.html")

@app.route('/free_code')
def free_code():
    return render_template("free_code_page.html")

@app.route('/lessons')
def lessons():
    return render_template("lessons_page.html")

@app.route('/lesson/<id>')
def lesson(id):
    return render_template("lessons/" + id + ".html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
