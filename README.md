# Python Test

I had to run almost everything in one day because most of 
my weekend was occupied with trying to collect my `PVC`

> Important: All commands show here must be run from the root directory

## Installing

```shell
git clone https://github.com/kosiken/umba_test.git
```

if you do not have `virtulenv` installed then install it

```shell
pip install virtualenv
```
finally run

```shell
cd umba_test
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Technologies used 

- Flask
- Flask-Migrate
- Flask-SQLAlchemy
- Flask-Caching


## Steps to run application

This app requires a `.env` file to be defined in the app directory as such

```shell
touch app/.env
```

You can refer to the `app/.env.example` file for some starter values

Before you run this app please do the following

> Make sure you have a redis server running or set CACHE=no in your .env or environment

you could run the script `initdb.sh` or run the following

```shell
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```
This is so that the database of the app can be initialized


To run the development server please run this command

```shell
python manage.py run
```

## Running tests

To run tests just run

```shell
python manage.py test
```

## Building docker image

To build a docker image please first create a `server.env` file in the root directory
check the `server.env.example` file to checkout the configurations
then run the following to build the image

```shell
docker build -t umba_test:local --target production . 
```

finally run whenever you want to deploy

```shell
docker run -d -p 3003:3003 --name umba-api --env-file server.env umba_test:local  
```
to create a container

## App structure

The **app** directory contains all the code that the flask server \
needs to run. 

```
app/
├── controllers/
├── main/
│   └── database/
├── models/
│   ├── __pycache__/
├── utils/
└── views/
    ├── layouts/
    ├── pages/
    └── partials/

```

The structure follows the MVC structure popular in Node.js express apps 

The controllers directory contains request handlers which are registered in the routes.py
file

The views directory contains static jinja templates

The utils directory contains helper classes 

The models directory contains database models


