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
- run `python manage.py createsuperuser` to create a super user
- run `python manage.py runserver 0.0.0.0:8000` to start the local development server
- visit `http://localhost:8000/admin` to login as super user
- visit `http://localhost:8000` to see standard django-webix package
- visit `http://localhost:8000/webix-admin/` to see django-webix admin sub-package
