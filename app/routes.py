from app import App
from flask import render_template

@App.route('/')
def index():
    return render_template('index.html')