# Simple Todo List API

Supports standard CRUD operations for managing database through a REST API
Utilizes function based api views
Uses Django's built in sqlite database

## Usage
```
# clone the repo
cd todoapi/
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```
