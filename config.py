__author__ = 'vitor'

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my very secret key'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    IMAGE_ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
    IMAGES_UPLOAD_FOLDER = os.path.realpath('.') + '/app/static/uploads/images'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'mysql://root:@localhost/dev-flask-jquery-fileupload'
    DEFAULT_FILE_STORAGE = 'filesystem'

config = {
    'development': DevelopmentConfig
}