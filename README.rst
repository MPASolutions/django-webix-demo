.. _Webix: https://webix.com

Django Webix Demo
=================

Sample project to use the Webix JavaScript UI library with Django (django-webix package).


Installation
------------

- run `virtualenv venv` to create a virtual environment
- run `source venv/bin/activate` to start the virtual environment
- run `pip install -r requirements.txt` to install all requirements
- run `python manage.py migrate` to run database migrations
- run `python manage.py loaddata data.json` to load the samples data
- add `webix` static files in `staticfiles/webix/`
- put http://code.jquery.com/jquery-3.2.1.min.js into `staticfiles/webix/`
- run `python manage.py runserver 0.0.0.0:8000` to start the local development server
- visit `http://localhost:8000`
