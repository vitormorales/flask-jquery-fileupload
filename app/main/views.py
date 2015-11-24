__author__ = 'vitor'

from app.models import Image
from flask.globals import request
from flask import render_template
from . import main


@main.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        file = request.files.getlist('file')
        image = Image()
        image.save(file[0])
    return render_template('upload.html')



