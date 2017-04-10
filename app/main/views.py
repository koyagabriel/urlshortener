# coding=utf-8
from flask import (render_template, request)
from flask_login import login_required, logout_user

from . import main
from .forms import RegistrationForm, LoginForm


@main.route('/')
@main.route('/index/')
@main.route('/register/')
@main.route('/login/')
def index():
    register_form = RegistrationForm()
    login_form = LoginForm()
    context = {"title": "Url Shortener", "registerForm": register_form,
               "loginForm": login_form}
    return render_template("index.html", context=context)


@main.route('/dashboard/', methods=["GET", "POST"])
@login_required
def dashboard():
    logout_user()
    return render_template('homepage.html')
