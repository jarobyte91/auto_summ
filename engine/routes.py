from flask import render_template, url_for, redirect, request, flash
from engine import app, db
from engine.forms import InputForm, ResponseForm
from engine.core.engine_summarization import algorithm
from engine.models import Query, Response

@app.route("/")
def index():
    return render_template("index.html", title = "Home")

@app.route("/summarization", methods = ["GET", "POST"])
def summarization():
    f = InputForm()
    if f.validate_on_submit():
        q = Query(text = request.form["input_text"], id = Query.query.count())
        db.session.add(q)
        db.session.commit()
        return redirect(url_for("summarization_response"))
    return render_template("summarization.html", form = f, title = "Summarization")

@app.route("/summarization_response", methods = ["GET", "POST"]) 
def summarization_response():
    text = Query.query.order_by(Query.id.desc()).first().text
    centralities = algorithm(text)
    # b = [{"rank":i, "sentence":sentences[j], "centrality":centralities[j]} 
    #      for i, j in enumerate(centralities.head().index.to_list(), 1)]
    b = centralities\
        .sort_values("centrality", ascending = False)\
        .assign(rank = lambda df: (df.index + 1).map(lambda x: f"{x:0>3}"),
                centrality = lambda df: df["centrality"].map(lambda x: f"{x:>.2f}"))\
        .to_dict("records")
    f = ResponseForm()
    if f.validate_on_submit():
        r = Response(id = Response.query.count(), text = text, 
                     summary = "".join([s["sentence"].replace("'", "''") 
                                        for s in b]), 
                     relevance = f.satisfaction.data)
        db.session.add(r)
        db.session.commit()
        flash("Thanks for your submission!")
        redirect(url_for("summarization"))
    return render_template("response.html", form = f, body = b, title = "Your Summary")

@app.route("/about_me")
def about_me():
    return render_template("about_me.html")
