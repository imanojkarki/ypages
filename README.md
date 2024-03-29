
# YellowPage (ypages) - A sample web-based Telephone Directory

[![Python Version](https://img.shields.io/badge/python-3.6-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-2.0-brightgreen.svg)](https://djangoproject.com)

This is a simple telephone directory written with Python/Django framework using Bootstrap (v4), jQuery (v3.2.1), FontAwesome (v5.0.6) and SQLite database.

It is a very small project of which was developed myself as part of my learning process. I am very new to Python/Django - just 4 months as of this posting. Hope someone may find it little useful.

## Features
1. Single Class Based View for Create, Read, Update and Delete Operations
2. Re-use of deleted record

### Screenshots
You may want to take a look at this sample site: [http://imanojkarki.pythonanywhere.com/](http://imanojkarki.pythonanywhere.com/ "YPage Sample Site") 

### Home/Front Page
![alt text](https://github.com/imanojkarki/ypages/blob/master/screenshot/ypages.JPG "YPages - Home/Main Page Screen")

### Category List
![alt text](https://github.com/imanojkarki/ypages/blob/master/screenshot/category_list.JPG "YPages - Screenshot of Category List")

### Category Form
![alt text](https://github.com/imanojkarki/ypages/blob/master/screenshot/category_form.JPG "YPages - Screenshot of Category Form")

### Contact List
![alt text](https://github.com/imanojkarki/ypages/blob/master/screenshot/contact_list.JPG "YPages - Screenshot of Contact List")

### Contact Form
![alt text](https://github.com/imanojkarki/ypages/blob/master/screenshot/contact_form.JPG "YPages - Screenshot of Contact Form")


## Installation 
 
Before following the steps below, make sure you have a recent version of Python (minimum 3.6.4) installed in your computer. 

Clone this repository:
```
git clone https://github.com/imanojkarki/ypages.git
CD ypages
```

create and start a a virtual environment

```
Linux$ sudo apt-get install virtualenv && virtualenv env
Linux$ source env/bin/activate
```

or 

```
Windows> python -m venv myspace
Windows> myspace/script/activate
``` 

Activate the virtualenv (always do this before working on the project),


Install python packages in the local env

```pip install -r requirements.txt```

Apply migrations

```python manage.py makemigrations```

Create a database (default is sqlite),

```python manage.py migrate```
 
Create a superuser (optional) - this allows you to login at the website as superuser and view the admin page.

```python manage.py createsuperuser```
 
If all went well then ready? Go!
 
```python ./manage.py runserver```

and then enter URL http://localhost:8000 in your web browser to view the app. 

