from flask import render_template, url_for, redirect, request, flash
from engine import app, db
from engine.forms import InputForm, ResponseForm
from engine.core.engine_summarization import algorithm

@app.route("/")
def index():
    return redirect(url_for("summarization"))

@app.route("/summarization", methods = ["GET", "POST"])
def summarization():
    f = InputForm()
    if f.validate_on_submit():
        db.engine.execute("INSERT INTO inputs (text) VALUES ('{}')".format(request.form["input_text"].replace("'", "''")))
        return redirect(url_for("summarization_response"))
    return render_template("summarization.html", form = f)

@app.route("/summarization_response", methods = ["GET", "POST"]) 
def summarization_response():
    record = list(db.engine.execute("SELECT * FROM inputs ORDER BY id DESC LIMIT 1"))
    text = record[0][1]
    sentences, centralities = algorithm(text)
    b = [{"rank":i, "sentence":sentences[j]} for i, j in enumerate(centralities.head().index.to_list(), 1)]
    f = ResponseForm()
    if f.validate_on_submit():
        query = """INSERT INTO responses (query, summary, relevance)
                   VALUES ('{}', '{}', {})""".format(text.replace("'", "''"), 
                                                 "".join([s["sentence"].replace("'", "''") for s in b]), 
                                                 f.satisfaction.data)
        db.engine.execute(query)
        flash("Thanks for your submission!")
        redirect(url_for("summarization"))
    return render_template("response.html", form = f, body = b)

