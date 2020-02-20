from flask import render_template, request, redirect, url_for, flash, abort
from . import main

@main.route('/')
def index():
    title = 'Home | Hype App'

    return render_template('index.html', title=title)