# Potion Social NodeJS Twitter like

This example built with Django and Python, shows you how you can use [Potion Social API](https://potion.social/ "Potion Social API") to build a twitter like stream. It is a really basic app allowing you to post a status, list them, like them, delete them and change your current user session.

## Install

`python -m pip install`

## Configure

Open `python_twitter_example/settings_local_template.py`  and fill it with your Potion Social Credentials, if you do not own credentials, create a free account on [Potion Social API Builder](https://api.potion.social/ "Potion Social API Builder").

Final `settings_local.py` file should look a bit like this :

```
PROJECT_URL = "https://mynetwork.potion.social"
API_KEY = "wDKAcGDe5SDSqZPlSd4G6Q"
API_SECRET = "cSJq56ZahNT_ZYOsUle43Q"
```

Once done, rename the file to `settings_local.py` and run the app.

## Run

`python manage.py runserver`

## Extend

Do not hesitate to extend this example or to send us your application using Potion Social API.
