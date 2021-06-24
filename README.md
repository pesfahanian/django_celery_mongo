# django_celery_mongo

Experimenting with exporting Django-celery results and logs to a MongoDB database.

This application is developed using:
- [Django](https://www.djangoproject.com/)
- [Celery](https://docs.celeryproject.org/en/stable/) - [Redis](https://redis.io/)
- [MongoDB](https://www.mongodb.com/)

## Usage
- Create a virtual environment:
    ```shell
    $ python -m venv .venv
    ```
- Activate the virtual environment:
    ```shell
    $ source .venv/bin/activate
    ```
- Install the required packages:
    ```shell
    $ pip install -r requirements.txt
    ```
- Apply Django migrations:
    ```shell
    $ python manage.py migrate
    ```
- Create a super-user:
    ```shell
    $ python manage.py createsuperuser
    ```
- Start the Celery worker (make sure you have Redis installed):
    ```shell
    $ celery -A backend.celery worker -l info
    ```
- In a separate terminal, run server:
    ```shell
    $ python manage.py runserver
