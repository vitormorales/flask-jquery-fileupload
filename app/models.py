__author__ = 'vitor'

import datetime
import os
from flask.globals import current_app
from werkzeug.utils import secure_filename
from app import db
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String, Date


class Image(db.Model):
    __tablename__ = 'images'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)
    image_path = Column(String(255), unique=True, nullable=False)
    created_at = Column(Date, default=datetime.datetime.now())
    updated_at = Column(Date, onupdate=datetime.datetime.now())

    def save(self, file):
        if file and Image.allowed_image(file.filename):
            filename = secure_filename(file.filename)
            try:
                path = os.path.join(current_app.config['IMAGES_UPLOAD_FOLDER'], filename)
                self.name = filename
                self.image_path = path
                db.session.add(self)

                file.save(path)
            except Exception as e:
                raise e

    @staticmethod
    def allowed_image(filename):
        return '.' in filename and \
            filename.rsplit('.', 1)[1] in current_app.config.get('IMAGE_ALLOWED_EXTENSIONS')