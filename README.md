# django-baby-steps
This repository represents the first baby steps I took to learn the Django Framework

## Pip
```
$ python3 -m venv djangox

$ source djangox/bin/activate
(djangox) $ pip install -r requirements.txt
(djangox) $ python manage.py migrate
(djangox) $ python manage.py createsuperuser
(djangox) $ python manage.py runserver

# Access the site at http://127.0.0.1:8000
```

## Pipenv
```
$ pipenv install

$ pipenv shell
(djangox) $ python manage.py migrate
(djangox) $ python manage.py createsuperuser
(djangox) $ python manage.py runserver

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

