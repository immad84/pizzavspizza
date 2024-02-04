

# Django REST framework installation

pip install djangorestframework

Do not forget to add djangorestframework to requirements.txt because
later when we go into production, we would need to install the version we
used in the development mode.
pip freeze > requirements.txt

As a Django extension, Django REST has to be added to the
INSTALLED_APPS list, rest_framework, in the settings.py file

