# ypages
<h1>YellowPage (ypages) - A sample web-based Telephone Directory</h1>

This is a simple telephone directory written with Python/Django framework using Bootstrap (v4), jQuery (v3.2.1), FontAwesome (v5.0.6) and SQLite database.

It is a very small project of which was developed myself as part of my learning process. I am very new to Python/Django - just 4 months as of this posting. Hope someone may find it little useful.

<h2>Installation</h2> 
 
Before following the steps below, make sure you have a recent version of Python (minimum 3.6.4) installed in your computer. 

```
Clone this repository: git clone https://github.com/imanojkarki/ypages.git
CD ypages
```

create and start a a virtual environment
```apt-get install virtualenv (Linux) ```
or 
```pip install virtualenv (Windows)```
 
Activate the virtualenv (always do this before working on the project),
```source env/bin/activate```
 
Install python packages in the local env
```pip install -r requirements.txt```
 
Create a database (default is sqlite),
```python manage.py migrate```
 
Create a superuser (optional) - this allows you to login at the website as superuser and view the admin page.
```python manage.py createsuperuser```
 
If all went well then ready? Go!
 
```./manage.py runserver```
and then enter URL http://localhost:8000 in your web browser to view the app. 

