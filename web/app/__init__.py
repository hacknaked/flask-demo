# coding=utf-8

from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from settings import API_PREFIX


def register_all(flask_app):
    """
    Register blueprints and deploy models into DB.
    """
    from tasks.controllers import tasks
    flask_app.register_blueprint(tasks, url_prefix=API_PREFIX + '/tasks')
    db.create_all()

app = Flask(__name__)
app.config.from_object('app.settings')
db = SQLAlchemy(app)
register_all(app)

@app.route("/")
def hello():
    return render_template('index.html')



