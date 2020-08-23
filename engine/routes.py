from flask import render_template, url_for, redirect, request, flash
from engine import app, db
from engine.forms import InputForm, ResponseForm
from engine.core.engine_summarization import algorithm
from engine.models import Query, Response

@app.route("/")
def index():
    return redirect(url_for("summarization"))

@app.route("/summarization", methods = ["GET", "POST"])
def summarization():
    f = InputForm()
    if f.validate_on_submit():
        q = Query(text = request.form["input_text"], id = Query.query.count())
        db.session.add(q)
        db.session.commit()
        return redirect(url_for("summarization_response"))
    return render_template("summarization.html", form = f)

@app.route("/summarization_response", methods = ["GET", "POST"]) 
def summarization_response():
    text = Query.query.order_by(Query.id.desc()).first().text
    sentences, centralities = algorithm(text)
    b = [{"rank":i, "sentence":sentences[j]} for i, j in enumerate(centralities.head().index.to_list(), 1)]
    f = ResponseForm()
    if f.validate_on_submit():
        r = Response(id = Response.query.count(), text = text, summary = "".join([s["sentence"].replace("'", "''") for s in b]), relevance = f.satisfaction.data)
        db.session.add(r)
        db.session.commit()
        flash("Thanks for your submission!")
        redirect(url_for("summarization"))
    return render_template("response.html", form = f, body = b)

