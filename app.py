from flask import Flask
from data.tasks import tasks

app = Flask(__name__)

@app.route("/")
def index():
    hello = 'Hello World'
    return hello

@app.route("/tasks")
def get_tasks():
    return tasks