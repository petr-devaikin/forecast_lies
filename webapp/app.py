from flask import Flask, render_template, request, url_for

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('application.cfg', silent=True)


@app.route('/')
def index():
    return "hello"