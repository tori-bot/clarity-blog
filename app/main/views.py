from django.shortcuts import render
from flask import render_template,redirect,url_for,abort
from . import main
from flask_login import current_user

@main.route('/')
def index():
    title='Clarity Blogs'
    return render_template('welcome.html',title=title)

    #adminprofile  