from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html.jinja")

@app.route('/about')
def about():
    return render_template("about.html.jinja")

@app.route('/contact')
def contact():
    return render_template("contact.html.jinja")

@app.route('/offer')
def offer():
    return render_template("offer.html.jinja")

@app.route('/portfolio')
def portfolio():
    return render_template("portfolio.html.jinja")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
