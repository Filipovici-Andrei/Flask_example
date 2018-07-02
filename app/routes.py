from flask import Blueprint, jsonify, url_for, flash, redirect
from flask import render_template

from app.forms.login import LoginForm

app_login = Blueprint("app", __name__,
                      template_folder="templates")


@app_login.route('/')
def hello():
    return render_template('home.html')
    # return jsonify({'message': 'Hello world!'})


@app_login.route('/login', methods=['POST', 'GET'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            login_form.username.data, login_form.submit.data))
        return redirect('/')
    return render_template('login.html', title='Sign in', form=login_form)


@app_login.route('/index')
def index():
    user = {'username': 'Mariusica'}
    posts = []
    for i in range(100):
        posts.extend([{
            'author': {'username': 'Jan'},
            'body': 'Bla, bla, bla'
            }, {
            'author': {'username': 'Dorel'},
            'body': 'A beautiful day'
            }])
    return render_template('index.html', user=user, posts=posts)
