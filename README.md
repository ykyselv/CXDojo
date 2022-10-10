# Django Application

### CXDojo Test

CXDojo Test task

## Goals

Understand how to work with databases, requests, http protocol.

## RUN

#### Install all dependencies:
pip install -r requirements.txt

#### copy .env.example
cp .env.example .env
#### make migrations:
python3 manage.py makemigrations

#### roll up migrations
python3 manage.py migrate

#### run server
python3 manage.py runserver

