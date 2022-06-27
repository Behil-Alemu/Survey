from ast import increment_lineno
import imp
from flask import Flask, Response, request, render_template, redirect, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import Question, Survey, satisfaction_survey as survey

app = Flask(__name__)

app.config['SECRET_KEY'] = "NA"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

Responses =[]

@app.route('/')
def survey_home():
    """Shows home page"""
    # survey = list(Survey)
    return render_template('survey.html', survey=survey)

@app.route("/start", methods=["POST"])
def start_survey():
    """Response can start from an empty array.No responses yet"""

    session[Responses] = []

    return redirect("/questions/0")


@app.route('/question/<int:id>')
def start_question(id):
    """Pulls up the first question from survey.py"""
    question = survey.questions[id]
    return render_template('question.html', survey=survey, question_num=id, question=question)
