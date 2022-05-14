from django.shortcuts import render
from flask import render_template,redirect,url_for,abort
from . import main

@main.route('/')
def index():
    title='Clarity Blogs'
    return render_template('index.html',title=title)