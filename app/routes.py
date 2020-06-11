# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'МАМА'}
    posts = [
        {
            'author': {'username': 'Vivaldi'},
            'body': 'The greatest blog!'
        },
        {
            'author': {'username': 'Jackie'},
            'body': 'The world won\'t be as a previous.'
        },
        {
            'author': {'username': 'Brazil'},
            'body': 'Python is the method only ;)'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)