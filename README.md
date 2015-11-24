#  Flask + JQuery File Upload + Bootstrap

This a sample of upload with

* Flask -> http://flask.pocoo.org/docs/0.10/
* JQuery File Upload -> https://github.com/blueimp/jQuery-File-Upload
* JavaScript Load Image -> https://github.com/blueimp/JavaScript-Load-Image
* Bootstrap 3 -> http://getbootstrap.com/
* MySQL

Be free to make sugestions and comment.

# How to run

1. Download the project.
2. Activate virtualenv: <code> source ~/flask-jquery-fileupload/venv/bin/activate </code>
3. Install requirements.txt (just to be sure): <code> pip install requirements.txt </code>
4. Create schema in MySQL called dev-jquery-fileupload (or just configure in project as you wish)
5. Init database: <code> ~/flask-jquery-fileupload/manage.py db init </code>
6. Migrate: <code> ~/flask-jquery-fileupload/manage.py db migrate </code>
7. Run server: <code> ~/flask-jquery-fileupload/manage.py runserver </code>

