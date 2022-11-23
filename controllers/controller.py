from flask import render_template, request # ADDED
from app import app
from models.question_list import questions
from models.question import Question

@app.route('/')
def index():
    return render_template('index.html', title='Home', questions=questions)

@app.route("/", methods=['GET', 'POST'])
def correct_answer():
    if request.method == 'POST':
        if request.form.get('action1') == 'Porsche':
            return "correct!" # do something
        else:
            return "False!" # unknown
    elif request.method == 'GET':
        return render_template('index.html', title='Home', questions=questions)
    
    return render_template("index.html")