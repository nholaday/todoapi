# Simple Todo List API

Uses Django's built in sqlite database

Supports standard CRUD operations for managing database through a REST API

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
