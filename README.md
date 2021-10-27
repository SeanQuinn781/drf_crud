# Django REST Framework CRUD Application - A minimal CRUD API based on the official DRF tutorial


## Installation

1) Enter the repository, create and activate a virtual environment


```
cd drf_crud 
python3 -m venv venv && source venv/bin/activate
```

2) Install the app requirements


```
pip3 -r requirements.txt
```

Optional: If you would like to upgrade the dependencies after installing them, you can use pur to bring requirements.txt to the latest version


```
pur -r requirements.txt
```

3) Run the migrations


```
python3 manage.py migrate
```

4) Run the application


```
python3 manage.py runserver
```

### Usage
Navigate to http://127.0.0.1:8000/api/customers/?format=api in your browser to see the customers list

Navigate to http://127.0.0.1:8000/api/customers/4/ to view an individual customer

For more examples check out the requests used in:
drf_crud/customers/tests.py and drf_crud/customers/tests.sh


### Resources
This project is a minimal version of the app demonstrated in the Django REST framework documentation 

For more information see:
https://www.django-rest-framework.org/tutorial/quickstart/

TODO: The python linters black and flake8 are installed and configured by pre-commit to autoformat files on every commit 

For more information see:
https://ljvmiranda921.github.io/notebook/2018/06/21/precommits-using-black-and-flake8/

### Libraries
https://github.com/psf/black
https://github.com/PyCQA/flake8
https://github.com/pre-commit/pre-commit

The .gitignore file was taken from:
https://djangowaves.com/tips-tricks/gitignore-for-a-django-project/

