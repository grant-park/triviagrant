from flask import Flask, url_for, request, render_template
from application import application
import redis

@application.route('/', methods=['GET', 'POST'])
def submit():
    if request.method == 'GET':
        return render_template('CreateQuestion.html');
    elif request.method == 'POST':
        question = request.form['question'];
        answer = request.form['answer'];
        title = request.form['title'];

        r.set(title+':question',question);
        r.set(title+':answer',answer);      

        return render_template('CreatedQuestion.html',
                               question = question, title = title);
    return;

@application.route('/about')
def about():
    url = url_for('/')
    link = '<a href="' + url + '">Play Game!</a>';
    return link;


@application.route('/question/<title>', methods=['GET', 'POST'])
def question(title):
    if request.method == 'GET':
        question = r.get(title+':question')
        return render_template('AnswerQuestion.html',
                               question = question)
    elif request.method == 'POST':
        submittedAnswer = request.form['submittedAnswer'];

        answer=r.get(title+':answer')

        if submittedAnswer == answer:
            return render_template('Correct.html');
        else:
            return render_template('Incorrect.html',
                                   answer = answer,
                                   submittedAnswer = submittedAnswer);
