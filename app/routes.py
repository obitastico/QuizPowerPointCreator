from comtypes import CoInitialize
from flask import render_template, request, session, redirect, url_for, flash, send_file

from app import app, check_iterable
from quizpptx import create_quiz_from_questions


@app.route('/', methods=['GET', 'POST'])
def index():
    """Callback for root page"""
    try:
        question = {
            "title": request.form["title"],
            "richtig": request.form["richtig"],
            "falsch": [request.form[key] for key in request.form if key.startswith("falsch")]
        }
        if check_iterable(question):
            session["questions"] = session.get("questions", [])
            session["questions"].append(question)
        else:
            if "finish" not in request.form:
                flash("Ein Textfeld wurde nicht ausgefüllt", "error")
        if "finish" in request.form:
            return redirect(url_for("download"))
    except KeyError:
        pass
    return render_template('index.html')


@app.route('/download')
def download():
    """Callback for download page"""
    return render_template("download.html")


@app.route('/download/quiz')
def download_quiz():
    """Returns the finished powerpoint"""
    try:
        CoInitialize()
        create_quiz_from_questions(session.get("questions", {}))
        session.pop('_flashes', None)
        try:
            del session["questions"]
        except KeyError:
            pass
        return send_file("../powerpoints/quiz.pptx", as_attachment=True)
    except Exception as e:
        return render_template("error.html", error=str(e))


    

