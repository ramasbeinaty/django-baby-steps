# django-baby-steps
This repository represents the first baby steps I took to learn the Django Framework

## Pip
```
$ python3 -m venv djangenv

$ source djangenv/bin/activate
(djangenv) $ pip install -r requirements.txt
(djangenv) $ python manage.py migrate
(djangenv) $ python manage.py createsuperuser
(djangenv) $ python manage.py runserver

# Access the site at http://127.0.0.1:8000
```

## Pipenv
```
$ pipenv install

$ pipenv shell
(djangenv) $ python manage.py migrate
(djangenv) $ python manage.py createsuperuser
(djangenv) $ python manage.py runserver

# Access the site at http://127.0.0.1:8000
```

# Setup
```
# Run Migrations
(djangoenv) $ python manage.py migrate

# Create a Superuser
(djangoenv) $ python manage.py createsuperuser

# Run the server to make sure everything is working:
(djangoenv) $ python manage.py runserver

# Access the site at http://127.0.0.1:8000/index
```

