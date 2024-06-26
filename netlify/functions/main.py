import awsgi
from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
import datetime

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def home():
    return render_template('home.html', date=datetime.datetime.now().year)


@app.route('/education')
def education():
    return render_template('education.html')


@app.route('/experience')
def experience():
    return render_template('experience.html')


def handler(event, context):
    return awsgi.response(app, event, context)


if __name__ == '__main__':
    app.run()
