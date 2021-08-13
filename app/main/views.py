from flask import render_template
from . import main

# Views
@main.route('/')
def index():
    '''
    View root function for homepage
    '''
    return render_template('index.html')