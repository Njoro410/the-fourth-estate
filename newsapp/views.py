from flask import Blueprint

views = Blueprint('views',__name__)

@views.route('/')
def index():
    return '<h1>hello world</h1>'
