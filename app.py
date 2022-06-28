from ast import increment_lineno
from http.client import responses
import imp
from urllib import response
from flask import Flask, Response, request, render_template, redirect, session,flash
from flask_debugtoolbar import DebugToolbarExtension
from surveys import Question, Survey, satisfaction_survey as survey

app = Flask(__name__)

app.config['SECRET_KEY'] = "NA"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

# Responses =[]

@app.route('/')
def survey_home():
    """Shows home page"""
    # survey = list(Survey)
    return render_template('survey.html', survey=survey)

@app.route("/start", methods=["POST"])
def start_survey():
    """Response can start from an empty array.No responses yet"""

    session["Responses"] = []

    return redirect("/questions/0")


@app.route('/questions/<int:id>')
def start_question(id):
    """Pulls up the first question from survey.py"""
    responses = session['Responses']
    if (responses is None):
        return redirect('/')
    elif len(responses) == len(survey.questions):
        return redirect('/alldone')
    elif len(responses) != id:
        flash('You are trying to access an invalid question')
        return redirect('/')
        

    question = survey.questions[id]
    return render_template('question.html', survey=survey, question_num=id, question=question)


@app.route('/answer',methods=["POST"])
def get_answer():
    """Add the response to session then redirect to question if not done"""
    input = request.form['answer']
    responses = session["Responses"]
    responses.append(input)
    session["Responses"] = responses


    if len(responses) == len(survey.questions):
        return redirect('/alldone')
    else:
        return redirect(f"/questions/{len(responses)}")


@app.route('/alldone')
def survey_done():
    '''Show the messege that it is all done '''
    return render_template('done.html')
