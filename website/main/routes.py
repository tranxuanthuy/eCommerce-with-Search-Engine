# các view function của blueprint main
from website.main import bp
from flask import render_template, url_for
@bp.route('/')
def index():
    return render_template('main/index.html')