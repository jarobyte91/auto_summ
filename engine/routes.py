from flask import render_template, url_for
from engine import app

@app.route("/")
@app.route("/main")
def main():
    return "Hello, world!"
