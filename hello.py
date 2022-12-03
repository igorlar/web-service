from flask import Flask
from flask import request
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def show_message():
    name = request.args.get('name', default = 'USER', type = str)
    message = request.args.get('message', default = 'HELLO', type = str)
    return f"<h2>Hello, {escape(name)}! {escape(message)}</h2>"

