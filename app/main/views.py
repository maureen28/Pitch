from flask import render_template,url_for, redirect
from . import main
from .forms import 
from flask_login import login_required

@main.route('/', methods = ['GET', 'POST'])
@login_required
def new_review(id):