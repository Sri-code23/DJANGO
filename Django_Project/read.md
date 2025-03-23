## Table of Contents

- [Table of Contents](#table-of-contents)
- [Creating a Directory for the Project](#creating-a-directory-for-the-project)
- [Creating a Virtual Environment](#creating-a-virtual-environment)
- [Activating the Virtual Environment](#activating-the-virtual-environment)
- [Installing the Required Packages](#installing-the-required-packages)
- [Creating a New Django Project](#creating-a-new-django-project)
- [Project Files Structure](#project-files-structure)
- [Directing into the Project Folder](#directing-into-the-project-folder)
- [Creating a New App in the Project](#creating-a-new-app-in-the-project)
- [App Structure](#app-structure)
- [Overall File Structure](#overall-file-structure)
- [Creating a Templates and Static Directory](#creating-a-templates-and-static-directory)
- [Templates Directory Structure](#templates-directory-structure)
- [Static Directory Structure](#static-directory-structure)
- [Configuring the Project to Use the Templates and Static Directories](#configuring-the-project-to-use-the-templates-and-static-directories)
- [Creating a View to Render the Home Page](#creating-a-view-to-render-the-home-page)
- [Creating a URL Pattern to Map to the View](#creating-a-url-pattern-to-map-to-the-view)
- [Including the App's URL Patterns in the Project's URL Patterns](#including-the-apps-url-patterns-in-the-projects-url-patterns)
- [Graph Diagrams](#graph-diagrams)
- [Settings.py](#settingspy)
- [mapping the request with relevant response](#mapping-the-request-with-relevant-response)
- [create a urls.py filein the My\_app dir](#create-a-urlspy-filein-the-my_app-dir)
- [now register the urls.py file in the main urls.py file](#now-register-the-urlspy-file-in-the-main-urlspy-file)
- [now run the server and check the url in the browser](#now-run-the-server-and-check-the-url-in-the-browser)
- [register the sttaic folder in the settings.py as done for templates,](#register-the-sttaic-folder-in-the-settingspy-as-done-for-templates)
- [now link the html and styles using the following code in the login.html file](#now-link-the-html-and-styles-using-the-following-code-in-the-loginhtml-file)
- [same is done for the signup.html](#same-is-done-for-the-signuphtml)
- [add as many views as you wish and update that in the both urls,urls.py](#add-as-many-views-as-you-wish-and-update-that-in-the-both-urlsurlspy)
- [redirect and reverse function](#redirect-and-reverse-function)
- [then declare the app\_name variablewith the app name](#then-declare-the-app_name-variablewith-the-app-name)
- [Layouts](#layouts)
- [include method for layout](#include-method-for-layout)
- [Variable interpolation](#variable-interpolation)
- [Filters](#filters)
- [for tags](#for-tags)
- [if tag](#if-tag)
- [url tag](#url-tag)
- [custom 404 page](#custom-404-page)
- [Logging](#logging)
- [connecting MySQL database](#connecting-mysql-database)
- [creating model](#creating-model)
- [creating migrations](#creating-migrations)
- [migrate](#migrate)
- [if you add a new column to the table](#if-you-add-a-new-column-to-the-table)
- [inserting data \& custom command](#inserting-data--custom-command)
- [getting post data](#getting-post-data)
- [getting data by Id](#getting-data-by-id)
- [redirect and reversing](#redirect-and-reversing)
- [GENERATE A SLUG FOR POST](#generate-a-slug-for-post)
- [creating category model](#creating-category-model)
- [linking (Many to one)](#linking-many-to-one)
- [deleting/recreating tables](#deletingrecreating-tables)
- [related posts](#related-posts)
- [Pagination](#pagination)

## Creating a Directory for the Project

To create a new directory for the project, use the `mkdir` command followed by the name of the directory. For example:

```bash
mkdir myproject
```

This will create a new directory named `myproject` in the current working directory.


## Creating a Virtual Environment

To create a new virtual environment, use the `python -m venv` command followed by the name of the virtual environment. For example:

```bash
python -m venv myenv
```

This will create a new virtual environment named `myenv` in the current working directory.

## Activating the Virtual Environment

To activate the virtual environment, use the following command:

```bash
myenv\Scripts\activate
```

On Windows, or:

```bash
source myenv/bin/activate
```

On macOS/Linux.

## Installing the Required Packages

To install the required packages, use the `pip install` command followed by the name of the package. For example:

```bash
pip install django
```

This will install the Django package and its dependencies.

## Creating a New Django Project

To create a new Django project, use the `django-admin startproject` command followed by the name of the project. For example:

```bash
django-admin startproject myproject
```

This will create a new Django project named `myproject` in the current working directory.

## Project Files Structure

The project files structure is as follows:

```python
myproject/
    manage.py
    myproject/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

## Directing into the Project Folder

To navigate into the project directory, use the `cd` command followed by the name of the directory. For example:

```bash
cd myproject
```

## Creating a New App in the Project

To create a new app in the project, use the `python manage.py startapp` command followed by the name of the app. For example:

```bash
python manage.py startapp myapp
```

This will create a new app named `myapp` in the project directory.

## App Structure

The app structure is as follows:

```python
myapp/
    __init__.py
    admin.py
    apps.py
    models.py
    tests.py
    urls.py
    views.py
    migrations/
        __init__.py
```

## Overall File Structure

The overall file structure is as follows:

```python
myproject/
    manage.py
    myproject/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
    myapp/
        __init__.py
        admin.py
        apps.py
        models.py
        tests.py
        urls.py
        views.py
        migrations/
            __init__.py
```

## Creating a Templates and Static Directory

To create a new directory for templates and static files, use the `mkdir` command followed by the name of the directory. For example:

```bash
mkdir myapp/templates
mkdir myapp/static
```

## Templates Directory Structure

The templates directory structure is as follows:

```python
myapp/
    templates/
        base.html
        home.html
```

## Static Directory Structure

The static directory structure is as follows:

```python
myapp/
   static/
        css/
            style.css
        js/
            script.js
        images/
            logo.png
```

## Configuring the Project to Use the Templates and Static Directories

To configure the project to use the templates and static directories, add the following lines to the `settings.py` file:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'myapp/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'myapp/static']
```

## Creating a View to Render the Home Page

To create a view to render the home page, add the following code to the `views.py` file:

```python
from django.shortcuts import render

def home(request):
    return render(request, 'myapp/home.html')
```

## Creating a URL Pattern to Map to the View

To create a URL pattern to map to the view, add the following code to the `urls.py` file:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

## Including the App's URL Patterns in the Project's URL Patterns

To include the app's URL patterns in the project's URL patterns, add the following code to the `myproject/urls.py` file:

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]
```



## Graph Diagrams

Here is a graph diagram of the project structure:
```
+---------------+
|  myproject   |
+---------------+
       |
       |
       v
+---------------+
|  myproject/  |
|  (project    |
|   directory)  |
+---------------+
       |
       |
       v
+---------------+
|  myapp/      |
|  (app        |
|   directory)  |
+---------------+
       |
       |
       v
+---------------+
|  templates/  |
|  (templates  |
|   directory)  |
+---------------+
       |
       |
       v
+---------------+
|  static/     |
|  (static     |
|   directory)  |
+---------------+
       |
       |
       v
+---------------+
|  views.py    |
|  (views file) |
+---------------+
       |
       |
       v
+---------------+
|  urls.py     |
|  (urls file)  |
+---------------+
```
Note: This is a simplified graph diagram and does not show all the files and directories in the project.

```
Note: This is a simplified graph diagram and does 
not show all the files and directories in the project.
```


## Settings.py

go to settings.py and add the following lines of code

```python
import os
```

next,add this in the templates 
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,"My_app/templates")],   
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
adding templates directory 
" os.path.join(BASE_DIR,"My_app/templates") "
we created in the file sructure using this line os.path.join(BASE_DIR)

the BASE_DIR is already defined in the settings.py file to point to the project root directory
```python
BASE_DIR = Path(__file__).resolve().parent.parent
```


## mapping the request with relevant response

go to views page 

define a response for a request 

```python
from django.shortcuts import render
def my_response(request):
    #return HttpResponse("Hello, world!")

    return render(request, 'login.html')
```

## create a urls.py filein the My_app dir

update the urls.py with the following code
```python
from django.urls import path
from . import views  

# . is nothing but the root directory of the project

urlpatterns = [
    path('my_response',views.my_response)
]
```


## now register the urls.py file in the main urls.py file

by using this code

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',include('My_app.urls')) #declaring the path for the urls.py file in the My_app dir
]
```



## now run the server and check the url in the browser


## register the sttaic folder in the settings.py as done for templates,
the code is written as,

```python
STATIC_URL = '/static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, "My_app/static")]

```

## now link the html and styles using the following code in the login.html file

```html

{% load static %} #loading the static files
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" 
     content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <link rel="stylesheet" href="{% static '/css/styles.css' %}"> #linking the styles.css file
</head>

```

## same is done for the signup.html


## add as many views as you wish and update that in the both urls,urls.py



## redirect and reverse function
in views.py
```python
from django.urls import reverse
```


## then declare the app_name variablewith the app name
in urls.py from my app, update
```python
app_name='Notes'
```

in views.py, we can write ,
```python
def old_url(request):
    return redirect(reverse('Notes:redirected_page'))
    #Note--name of the app declared in the urls.py
    #:name calling and redirecrting to the page using its name

def new_url_page(request):
    return HttpResponse("this is an New URL")
```

in urls.py,

 ```python
path('new_url',views.new_url_page,name="redirected_page")
```
using this,
the url becomes from this http://127.0.0.1:8000/old_url
to http://127.0.0.1:8000/new_url


## Layouts 

if we want to design or declare a common layout for all html files, we can do this by creating another html file like('base.html')

in base.html, apply where we want to apply the common layout
```html
{% block content %}
{% endblock %}
```

in index.html,
```html
{% extends 'base.html' %}
{% block content %}
<!--html file that extends the base.html-->
 {% endblock %}
```
## include method for layout

## Variable interpolation
for dynamic values(changing values),

if the values has to change...
in views.py
```python
def Http_response(request):
    name="Broskies"
    return render(request,'welcome_page.html',{"name":name})
```

in welcome_page.html,

```html
<body>
    <h2>Welcome {{name}} to the login page</h2>
</body>
```

## Filters
upper,
```html
<body>
    <h2>Welcome {{name | upper}} to the login page</h2>
</body>
```
length,
```html
<body>
    <h2>Welcome {{name | length}} to the login page</h2>
</body>
```
truncatewords(adds '...' after 1 word)
```html
<body>
    <h2>Welcome {{name | truncatewords:1}} to the login page</h2>
</body>
```
default,
```html
<body>
    <h2>Welcome {{name | default:"Document"}} to the login page</h2>
</body>
```

## for tags
```python
def Http_response(request):
    name="Broskies"
    Posts=[
        {"title":"Python","author":"Broskies"},
        {"title":"Django","author":"Broskies"},
        {"title":"Flask","author":"Broskies"},
    ]
    return render(request,'welcome_page.html',{"name":name,'posts':Posts})

```


```html
{% for post in Posts %}
<h2>{{post.title}}</h2>
<p>By {{post.author}}</p>
{% endfor %}

```

## if tag

```python
def Http_response(request):
    name="Broskies"
    Posts=[
        #empty#
    ]
    return render(request,'welcome_page.html',{"name":name,'posts':Posts})

```


```html
{% if Posts %} <!--if posts=True: -->
    {% for post in Posts %}
    <h2>{{post.title}}</h2>
    <p>By {{post.author}}</p>
    {% endfor %}
{% else %}
<h2>No posts available</h2>
{% endif %}
```


## url tag

```python
urlpatterns = [
    #mporting the response functions from the views file and addding it to the path
    path('',views.Http_response,name="base_page"),   
    path('login/',views.login_response, name="Login_page"),
    path('signup/',views.signup_response,name="signup_page"),
    path('old_url/',views.old_url,name="old_url"),
    path('new_url',views.new_url_page,name="redirected_page")
]
```
acccessing the name of the url path in the html file
```html
<div class="sign-up">
    <p>Don't have an  account?
        <!-- {% url 'app_name:name of url(path)%}--> 
    <a href="{% url 'Notes:signup_page' %}" >Sign Up</a>
    </p>
</div>
```


## custom 404 page 
first create a templates folder in the main root directory
then create a 404.html file inside the templates folder
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" 
     content="width=device-width, initial-scale=1.0">
    <title>Sign Up</title>
    <link rel="stylesheet" href="{% static '/css/styles.css' %}">
</head>
<body>
    <h1> page not found </h1>
    <h1> Custom page </h1>
</body>

```
then =create a new views.py in the main root directory and write the method,
```python
## custom error -- page not found error page(404)
def page_error(request,exception):
    return render(request,'404_page.html', status=404)
```


then add a 'handler404' variable in then main urls.py
```python
handler404='Django_app.views.page_error'
```

then in settings.py , change DEBUG=False

```python
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False #default value will be True


## and add this line to provide access to these hosts
ALLOWED_HOSTS = [
    '127.0.0.1','localhost'
]
```

add templates to  the TEMPLATES=[] in settings.py
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #add 'templates' in the dir list
        'DIRS': ['templates',os.path.join(BASE_DIR,"My_app/templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
## Logging 
```
???
```

## connecting MySQL database

first install the 'mysqlclient' package

```python
pip install mysqlclient
```
then in settings.py add the following lines

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'notes',
        'USER': 'root',
        'PASSWORD': 'Sridhar@2312',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

## creating model
open models.py file ,
create a class 'name'
```python

from django.db import models

# Create your models here.
class User_database(models.Model):
    user_id=models.CharField(max_length=999,unique=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    content=models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    img_url=models.URLField(max_length=100)

    #not necessary 
    def __str__(self):
        return self.username

```

## creating migrations

in terminal , execute
```
python manage.py makemigrations
```

a initial file will be created in the migrations folder , this file is used to create the database table in the database.

#here an error occured
```cmd
(Myenv) C:\Users\vaath\OneDrive\Desktop\MY FILES\C O D E S\Django\Django_Project\Django_app> python manage.py makemigrations

WARNINGS:
?: (urls.W005) URL namespace 'Notes' isn't unique. You may not be able to reverse all URLs in this namespace
No changes detected

```

this occured due to that we forgot to add the app we created i.e the folder "My_app" 


```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'My_app', #added 'My_app',
]
```

now a file named '0001_initial.py' will be created in the migrations directory

```python
# 0001_initial.py
# Generated by Django 5.1.4 on 2024-12-17 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_database',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
```

this contains the detials of the model at iniial stage

## migrate
this will create the table inthe database

```bash
python manage.py migrate
```

```bash
(Myenv) C:\Users\vaath\OneDrive\Desktop\MY FILES\C O D E S\Django\Django_Project\Django_app> python manage.py migrate       
System check identified some issues:

WARNINGS:
?: (urls.W005) URL namespace 'Notes' isn't unique. You may not be able to reverse all URLs in this namespace
Operations to perform:
  Apply all migrations: My_app, admin, auth, contenttypes, sessions
Running migrations:
  Applying My_app.0001_initial... OK
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
```

several tables will be created in the database like seen above

* if you want to make any changes to the table
* make the changes and do the same process 
  ```
  python manage.py makemigrations
  ```
  this will create an another migration file named '0002_initial.py' with the changes made

-now run this again
```bash
python manage.py migrate
```
this will update the table with changes

## if you add a new column to the table
do this same process
"makemigrations"

this will ask you two options, 
```cmd
(Myenv) C:\Users\vaath\OneDrive\Desktop\MY FILES\C O D E S\Django\Django_Project\Django_app> python manage.py makemigrations
System check identified some issues:

WARNINGS:
?: (urls.W005) URL namespace 'Notes' isn't unique. You may not be able to reverse all URLs in this namespace
It is impossible to add the field 'created_at' with 'auto_now_add=True' to user_database without providing a default. This is because the database needs something to populate existing rows.
 1) Provide a one-off default now which will be set on all existing rows
 2) Quit and manually define a default value in models.py.
Select an option:
```
select-1 if the table doesnot have data
select-2 -to set a default value for the newly added column

```
Select an option: 1
Please enter the default value as valid Python.
Accept the default 'timezone.now' by pressing 'Enter' or provide another value.
The datetime and django.utils.timezone modules are available, so it is possible to provide e.g. timezone.now as a value.
Type 'exit' to exit this prompt
[default: timezone.now] >>> #just do enter
```
#just do enter button here 
*then migrate the changes,the table will be updated with the changes


## inserting data & custom command
* create a 'management' folder in the My_app dir
* create a 'commands' folder in the 'management' folder , bothe folder should have an '__init__.py' file
* create a file named 'populate_posts.py' in the 'commands' folder 
* write the following code in the file
  

```python
from typing import Any
from My_app.models import User_database
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help="inserting the data into the table"
    
    def handle(self, *args, **options):
        usernames = [
            "john_doe",
            "jane_smith",
            "bob_johnson",
            "alice_williams",
            "mike_davis",
            "emily_chen",
            "david_lee",
            "sarah_taylor",
            "kevin_white",
            "olivia_martin"
        ]
        emails=[
            "john_doe@example.com",
            "jane_smith@gmail.com",
            "bob_johnson@yahoo.com",
            "alice_williams@hotmail.com",
            "mike_davis@aol.com",
            "emily_chen@outlook.com",
            "david_lee@protonmail.com",
            "sarah_taylor@icloud.com",
            "kevin_white@zoho.com",
            "olivia_martin@yandex.com"
        ]
        passwords = [
            "P@ssw0rd123",
            "Giraffe#LemonTree88",
            "Tr0ub4d3!K1ng",
            "PineapplePizzaLover22",
            "SunnyDay123!",
            "BaseballFan42!",
            "ILoveDogs!",
            "CoffeeLover88",
            "Bookworm2000",
            "MusicIsLife123"
        ]
        img_urls=[
            "https://picsum.photos/id/1/800/400",
            "https://picsum.photos/id/2/800/400",
            "https://picsum.photos/id/3/800/400",
            "https://picsum.photos/id/4/800/400",
            "https://picsum.photos/id/5/800/400",
            "https://picsum.photos/id/6/800/400",
            "https://picsum.photos/id/7/800/400",
            "https://picsum.photos/id/8/800/400",
            "https://picsum.photos/id/9/800/400",
            "https://picsum.photos/id/10/800/400",
        ]


        for username,email,passw,img_url in zip(usernames,emails,passwords,img_urls):
            User_database.objects.create(username=username,email=email,password=passw,img_url=img_url)

        self.stdout.write(self.style.SUCCESS("Completed inserting ."))


```

in the commands '__init__.py' write the following command
```python
from .populate_posts import Command as PopulatePostCommand

```

the run the following command in the terminal 
```
python manage.py populate_posts
```
--now the data would be added to the database

## getting post data

now in 'views.py' of 'my_app'
add the following code---

```python
#adding dynamic data from the databse
from .models import User_database

def index(request):
    u_data=User_database.objects.all()
    return render(request,'index.html',{'database':u_data})

```

now the html files can be fed with the data

For example:
```html
{% load static %} <!--to load the static folder containing the stylesheets-->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blogs | Home</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="{% static 'css/index.css' %}">

</head>
<body>
    <header>
        <nav>
            <div class="logo">Blogs</div>
            <ul>
                <li><a href="#" class="active">Home</a></li>
                <li><a href="#">Categories</a></li>
                <li><a href="{% url 'Notes:signup_page' %}">Profile</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section class="hero">
            <h1>Welcome to Blogs</h1>
            <p>Explore the depths of knowledge in our dark-themed articles</p>
            <form class="search-form">
                <input type="search" placeholder="Search articles..." aria-label="Search articles">
                <button type="submit" aria-label="Submit search">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor"     stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <circle cx="11" cy="11" r="8"></circle>
                        <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                    </svg>
                </button>
            </form>
        </section>
        
        <section class="featured-posts">
            <h2>Top Users</h2>
            
            <div class="post-grid">
                {% for dta in database %}                   #<!-- foreach data in the databse imported fromthe views.py  -->
                <div class="post-card">
                    <img src="{{dta.img_url}}" alt="image">  #<!--placing the dta.argument i.e dta.img_url -->
                    <div class="post-content">
                        <h3>Username : {{dta.username}} </h3> #<!--placing the dta.argument i.e dta.email -->
                        <p>Email: {{dta.email}}</p>            #<!--placing the dta.argument i.e dta.username -->
                    </div>
                </div>
                {% endfor %}
            </div>
            
        </section>
    </main>



    <!-- footer -->
    <footer>
        <div class="footer-content">
            <div class="footer-section">
                <h3>About Dark Blog</h3>
                <p>Illuminating minds through dark-themed articles on technology, design, and development.</p>
            </div>
            <div class="footer-section">
                <h3>Quick Links</h3>
                <ul>
                    <li><a href="#">About Us</a></li>
                    <li><a href="#">Contact</a></li>
                    <li><a href="#">Privacy Policy</a></li>
                    <li><a href="#">Terms of Service</a></li>
                </ul>
            </div>
            <div class="footer-section">
                <h3>Connect With Us</h3>
                <div class="social-icons">
                    <a href="#" aria-label="Facebook">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path>
                        </svg>
                    </a>
                    <a href="#" aria-label="Twitter">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"></path>
                        </svg>
                    </a>
                    <a href="#" aria-label="Instagram">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect>
                            <path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path>
                            <line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line>
                        </svg>
                    </a>
                </div>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2024 Dark Blog. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>

```


now run the server using 
```bash
python manage.py runserver
```

you can see the web page


## getting data by Id


to get the data by id and display the information of that id is done by adding the folluwing view in 'views.py'

```python
#post_detail
def detail(request,post_id):
    #for static data
    """
    posts=[
        {'id':1,'title':'aaaa'},
        {'id':2,'title':'bbbb'},
        {'id':3,'title':'cccc'},
        {'id':4,'title':'dddd'},
        {'id':5,'title':'eeee'},
    ]
    next((i for i in posts if i['id']==id))
    """
    #for dynamic data
    user_data=User_database.objects.get(id=post_id)
    return render(request,'details.html',{'user_dat':user_data})

```

* then add a details.html page to display the info that id 
* here 'details.html' is used
* in html file
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User | details</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="{% static '/css/details.css' %}">
</head>
<body>
    <header>
        <nav>
            <div class="logo">Blogs</div>
            <ul>
                <li><a href="{% url 'Notes:det_to_basepage' %}">Home</a></li>
                <li><a href="categories.html">Categories</a></li>
                <li><a href="profile.html">Profile</a></li>
                <li><a href="login.html">Login</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <article class="blog-post">
            
            <h1>{{user_dat.username}}'s details</h1>
            <div class="meta">
                <span class="author">{{user_dat.username}}</span>
                <span class="date">{{user_dat.created_at }}</span>
                <span class="category">{{user_dat.email}}</span>
            </div>

            <img src="{{user_dat.img_url}}" alt="AI in Web Development" class="featured-image">
            <div class="content">
                <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. 
                    Modi, impedit molestiae cumque repellendus ex officia 
                    odio aliquid commodi voluptatibus minima hic explicabo 
                    facere nemo ipsa saepe?
                    Corporis adipisci eveniet voluptate.
                    Lorem ipsum dolor sit, amet consectetur adipisicing elit. 
                    odi, impedit molestiae cumque repellendus ex officia 
                    odio aliquid commodi voluptatibus minima hic explicabo 
                    facere nemo ipsa saepe?
                    Corporis adipisci eveniet voluptate.
                </p>
            </div>
        </article>

        <section class="comments">
            <h2>Comments</h2>
            <div class="comment-list">
                <div class="comment">
                    <img src="https://via.placeholder.com/300x200" alt="User avatar" class="comment-avatar">
                    <div class="comment-content">
                        <h3>Jane Smith</h3>
                        <p>This is a fascinating look into the future of web development. I'm particularly excited about the potential for AI to enhance accessibility.</p>
                        <span class="comment-date">Posted on May 16, 2024</span>
                    </div>
                </div>
                <div class="comment">
                    <img src="https://via.placeholder.com/300x200" alt="User avatar" class="comment-avatar">
                    <div class="comment-content">
                        <h3>Mike Johnson</h3>
                        <p>Great article! I'm curious about how AI might impact job prospects for web developers in the coming years. Any thoughts on that?</p>
                        <span class="comment-date">Posted on May 17, 2024</span>
                    </div>
                </div>
            </div>
            <form class="comment-form">
                <h3>Leave a Comment</h3>
                <div class="form-group">
                    <label for="name">Name</label>
                    <input type="text" id="name" name="name" required>
                </div>
                <div class="form-group">
                    <label for="email">Email</label>
                    <input type="email" id="email" name="email" required>
                </div>
                <div class="form-group">
                    <label for="comment">Comment</label>
                    <textarea id="comment" name="comment" rows="4" required></textarea>
                </div>
                <button type="submit" class="btn-submit">Post Comment</button>
            </form>
        </section>
    </main>

    <footer>
        <div class="footer-content">
            <div class="footer-section">
                <h3>About Dark Blog</h3>
                <p>Illuminating minds through dark-themed articles on technology, design, and development.</p>
            </div>
            <div class="footer-section">
                <h3>Quick Links</h3>
                <ul>
                    <li><a href="#">About Us</a></li>
                    <li><a href="#">Contact</a></li>
                    <li><a href="#">Privacy Policy</a></li>
                    <li><a href="#">Terms of Service</a></li>
                </ul>
            </div>
            <div class="footer-section">
                <h3>Connect With Us</h3>
                <div class="social-icons">
                    <a href="#" aria-label="Facebook">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path>
                        </svg>
                    </a>
                    <a href="#" aria-label="Twitter">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"></path>
                        </svg>
                    </a>
                    <a href="#" aria-label="Instagram">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect>
                            <path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path>
                            <line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line>
                        </svg>
                    </a>
                </div>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2024 Dark Blog. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>

```

## redirect and reversing
here we are trying to redirect the user to the home oage when he presses the home option in the details.html

* to do that 
```python
#views.py
def details_to_base(request):
    return redirect(reverse('Notes:base_page'))

```

* in urls.py
```python
#urls.py

urlpatterns = [
    #mporting the response functions from the views file and addding it to the path
    path('',views.index,name="base_page" ),
    path('post/<int:post_id>/',views.detail,name="Post_detail"),
    path('login/',views.login_response, name="Login_page"),
    path('signup/',views.signup_response,name="signup_page"),
    path('old_url/',views.old_url,name="old_url"),
    path('new_url',views.new_url_page,name="redirected_page"),
    path('home/', views.details_to_base,name="det_to_basepage"),### add this redirection path
]
```

## GENERATE A SLUG FOR POST

slug url - hiding the info displayed on the url by using an alternative

* First add a line in the populate_command.py
  
```python
def handle(self, *args, **options):
        #this line delets the existing data in the table
        User_database.objects.all().delete()
```


then add a column field in the table named slug
```python
from django.utils.text import slugify

    #Adding Slug column in the table
    sluged_text=models.SlugField(unique=True)


    def save(self,*args,**kwargs):
        self.sluged_text = slugify(self.username)
        super().save(*args,**kwargs)
```
after this run the command to make migrations
```
python manage.py makemigrations
```
* if it asks for the default value, then add a default value for the slugfield , by choosing the option-1 in the terminal output if it is asked
* new migrations file will be created in the 'migrations' folder
```python

# Generated by Django 5.1.4 on 2024-12-24 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('My_app', '0002_user_database_created_at_user_database_img_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_database',
            name='slug',
            field=models.SlugField(default='slug-example', unique=True),
            preserve_default=False,
        ),
    ]

```

*then migrate the changes using the command
```
python manage.py migrate
```

the table will be updated with the slugged values of the username

* if you get any error like the following error with the migrate opertion
```
(Myenv) C:\Users\vaath\OneDrive\Desktop\MY FILES\C O D E S\Django\Django_project\Django_app> python manage.py migrate
System check identified some issues:

WARNINGS:
?: (urls.W005) URL namespace 'Notes' isn't unique. You may not be able to reverse all URLs in this namespace
Operations to perform:
  Apply all migrations: My_app, admin, auth, contenttypes, sessions
Running migrations:
  Applying My_app.0003_user_database_sluged_text...Traceback (most recent call last):
  File "C:\Users\vaath\OneDrive\Desktop\MY FILES\C O D E S\Django\Myenv\Lib\site-packages\django\db\backends\utils.py", line 105, in _execute
    return self.cursor.execute(sql, params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\vaath\OneDrive\Desktop\MY FILES\C O D E S\Django\Myenv\Lib\site-packages\django\db\backends\mysql\base.py", line 76, in execute
    return self.cursor.execute(query, args)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\vaath\OneDrive\Desktop\MY FILES\C O D E S\Django\Myenv\Lib\site-packages\MySQLdb\cursors.py", line 179, in execute
    res = self._query(mogrified_query)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\vaath\OneDrive\Desktop\MY FILES\C O D E S\Django\Myenv\Lib\site-packages\MySQLdb\cursors.py", line 330, in _query
    db.query(q)
  File "C:\Users\vaath\OneDrive\Desktop\MY FILES\C O D E S\Django\Myenv\Lib\site-packages\MySQLdb\connections.py", line 265, in query
    _mysql.connection.query(self, query)
MySQLdb.IntegrityError: (1062, "Duplicate entry 'default-slug' for key 'my_app_user_database.sluged_text'")

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\vaath\OneDrive\Desktop\MY FILES\C O D E S\Django\Django_project\Django_app\manage.py", line 22, in <module>
    main()
  File "C:\Users\vaath\OneDrive\Desktop\MY FILES\C O D E S\Django\Django_project\Django_app\manage.py", line 18, in main
    execute_from_command_line(sys.argv)
  File "C:\Users\vaath\OneDrive\Desktop\MY FILES\C O D E S\Django\Myenv\Lib\site-packages\django\core\management\__init__.py", line 442, in execute_from_command_line    
    utility.execute()
  File "C:\Users\vaath\OneDrive\Desktop\MY FILES\C O D E S\Django\Myenv\Lib\site-packages\django\core\management\__init__.py", line 436, in execute
    self.fetch_command(subcommand).run_from_argv(self.argv)
  File "C:\Users\vaath\OneDrive\Desktop\MY FILES\C O D E S\Django\Myenv\Lib\site-packages\django\core\management\base.py", line 413, in run_from_argv
    self.execute(*args, **cmd_options)
  File "C:\Users\vaath\OneDrive\Desktop\MY FILES\C O D E S\Django\Myenv\Lib\site-packages\django\core\management\base.py", line 459, in execute
    output = self.handle(*args, **options)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\vaath\OneDrive\Desktop\MY FILES\C O D E S\Django\Myenv\Lib\site-packages\django\core\management\base.py", line 107, in wrapper
    res = handle_func(*args, **kwargs)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\vaath\OneDrive\Desktop\MY FILES\C O D E S\Django\Myenv\Lib\site-packages\django\core\management\commands\migrate.py", line 357, in handle
    post_migrate_state = executor.migrate(
                         ^^^^^^^^^^^^^^^^^
  File "C:\Users\vaath\OneDrive\Desktop\MY FILES\C O D E S\Django\Myenv\Lib\site-packages\django\db\migrations\executor.py", line 135, in migrate
    state = self._migrate_all_forwards(
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\vaath\OneDrive\Desktop\MY FILES\C O D E S\Django\Myenv\Lib\site-packages\django\db\migrations\executor.py", line 167, in _migrate_all_forwards
    state = self.apply_migration(
            ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\vaath\OneDrive\Desktop\MY FILES\C O D E S\Django\Myenv\Lib\site-packages\django\db\migrations\executor.py", line 255, in apply_migration
    state = migration.apply(state, schema_editor)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\vaath\OneDrive\Desktop\MY FILES\C O D E S\Django\Myenv\Lib\site-packages\django\db\migrations\migration.py", line 132, in apply
    operation.database_forwards(
  File "C:\Users\vaath\OneDrive\Desktop\MY FILES\C O D E S\Django\Myenv\Lib\site-packages\django\db\migrations\operations\fields.py", line 110, in database_forwards     
    schema_editor.add_field(
  File "C:\Users\vaath\OneDrive\Desktop\MY FILES\C O D E S\Django\Myenv\Lib\site-packages\django\db\backends\mysql\schema.py", line 113, in add_field
    super().add_field(model, field)
  File "C:\Users\vaath\OneDrive\Desktop\MY FILES\C O D E S\Django\Myenv\Lib\site-packages\django\db\backends\base\schema.py", line 768, in add_field
    self.execute(sql, params or None)
  File "C:\Users\vaath\OneDrive\Desktop\MY FILES\C O D E S\Django\Myenv\Lib\site-packages\django\db\backends\base\schema.py", line 202, in execute
    cursor.execute(sql, params)
  File "C:\Users\vaath\OneDrive\Desktop\MY FILES\C O D E S\Django\Myenv\Lib\site-packages\django\db\backends\utils.py", line 122, in execute
    return super().execute(sql, params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\vaath\OneDrive\Desktop\MY FILES\C O D E S\Django\Myenv\Lib\site-packages\django\db\backends\utils.py", line 79, in execute
    return self._execute_with_wrappers(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\vaath\OneDrive\Desktop\MY FILES\C O D E S\Django\Myenv\Lib\site-packages\django\db\backends\utils.py", line 92, in _execute_with_wrappers
    return executor(sql, params, many, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\vaath\OneDrive\Desktop\MY FILES\C O D E S\Django\Myenv\Lib\site-packages\django\db\backends\utils.py", line 100, in _execute
    with self.db.wrap_database_errors:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\vaath\OneDrive\Desktop\MY FILES\C O D E S\Django\Myenv\Lib\site-packages\django\db\utils.py", line 91, in __exit__
    raise dj_exc_value.with_traceback(traceback) from exc_value
  File "C:\Users\vaath\OneDrive\Desktop\MY FILES\C O D E S\Django\Myenv\Lib\site-packages\django\db\backends\utils.py", line 105, in _execute
    return self.cursor.execute(sql, params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\vaath\OneDrive\Desktop\MY FILES\C O D E S\Django\Myenv\Lib\site-packages\django\db\backends\mysql\base.py", line 76, in execute
    return self.cursor.execute(query, args)
  File "C:\Users\vaath\OneDrive\Desktop\MY FILES\C O D E S\Django\Myenv\Lib\site-packages\MySQLdb\cursors.py", line 179, in execute
    res = self._query(mogrified_query)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\vaath\OneDrive\Desktop\MY FILES\C O D E S\Django\Myenv\Lib\site-packages\MySQLdb\cursors.py", line 330, in _query
    db.query(q)
  File "C:\Users\vaath\OneDrive\Desktop\MY FILES\C O D E S\Django\Myenv\Lib\site-packages\MySQLdb\connections.py", line 265, in query
    _mysql.connection.query(self, query)
django.db.utils.IntegrityError: (1062, "Duplicate entry 'default-slug' for key 'my_app_user_database.sluged_text'")


```

if this happens , clear the migrations files that are created so far and start from first, 
by changing the model details,and run the 

```
python manage.py makemigrations
```
---now that 'slug' field is created in the table , use that data to get the detail by 'slug'
for example , in url when inspecting the detail of a particular post , it displays the post info, so to hide the info from users, we use slugs to represent the url

```
http://127.0.0.1:8000/post/11/
```

in the above url, we see the post no' 11' , this helps the hackers to gain access over the pos count, so we use slug for this, by following steps

* urls.py
```python
# urls.py

path('post/<str:slug>/',views.detail,name="Post_detail"),
```
* views.py
```python 
# views.py

def detail(request,slug):
    #for static data
    """
    posts=[
        {'id':1,'title':'aaaa'},
        {'id':2,'title':'bbbb'},
        {'id':3,'title':'cccc'},
        {'id':4,'title':'dddd'},
        {'id':5,'title':'eeee'},
    ]
    next((i for i in posts if i['id']==id))
    """
    #for dynamic data
    user_data=User_database.objects.get(slug=slug)
    return render(request,'details.html',{'user_dat':user_data})
    
```

* in html file
```html
<a href="{% url 'Notes:Post_detail' slug=dta.slug %}" class="read-more">read-more</a>
```

now the url is like this , represented with slug name

```
http://127.0.0.1:8000/post/john_doe/
```



## creating category model 
creating another model to handle categories


to create a new model (i.e a new table in the dtaabase to handle category section)


create a new class in the models.py
```python
# models.py

class category_table(models.Model):
    c_name=models.CharField( max_length=50)

    def __str__(self):
        return self.c_name

```
now run the command 
```

python manage.py makemigrations

```

then add the data to the 'managements/commands/' folder under a new file named 'populate_category'

```python 
from typing import Any
from My_app.models import category_table
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help="inserting the category data into the table"
    
    def handle(self, *args, **options):

        #this line delets the existing data in the table
        category_table.objects.all().delete()

        category_names=['manager','admin','employee','client']
        
        for category in category_names:
            category_table.objects.create(c_name=category)

        self.stdout.write(self.style.SUCCESS("Completed inserting categories .")) 
        
```

now in the '__init__.py ' file under the commands directory , add the following line

```python
from .populate_category import Command as PopulateCategoryCommand
```
now run the migrate command

```
python manage.py migrate
```
then run the folloowing command to add data to the categoty_table

```
python manage.py populate_category

```
now the data would be addded to the category table



## linking (Many to one)

to linke category table to the userdatabase table using foreign key ,
first in 'models.py' add,

```python 
from django.db import models
from django.utils.text import slugify

# Create your models here. 

class category_table(models.Model):
    c_name=models.CharField( max_length=50)

    def __str__(self):
        return self.c_name

class User_database(models.Model):
    #id=models.CharField(max_length=999,unique=True)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    #content=models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    img_url=models.URLField(max_length=100,null=True)
    #Adding Slug column in the table
    slug=models.SlugField(unique=True)
    #adding category tabel as a foreign key
    category_id=models.ForeignKey(category_table, on_delete=models.CASCADE, null=True)


    def save(self,*args,**kwargs):
        self.slug = slugify(self.username)
        super().save(*args,**kwargs)


    def __str__(self):
        return self.username
```

```
IMPORTANT NOTE:
Arrange the primary key table(i.e, category table) in the firt and the foreign key table in the seoond row  refer the above program

```

now run the commands 
```
python manage.py makemigrations
python manage.py migrate
```

the terminal will ask for an default value, enter a default value and proceed

--to alter the category id in the 'user_database table',

* then in the 'populate_posts.py' alter the program to add foreign key value ,
* for here we use random category
now in 'populatePosts.py' , alter things by
```python
import random

categories=category_table.objects.all()

for username,email,passw,img_url in zip(usernames,emails,passwords,img_urls):
category=random.choice(categories)
User_database.objects.create(username=username,email=email,password=passw,img_url=img_url,category_id=category)

```

* now run the command
```
python manage.py populate_posts
```now the category_id are filled withrandom category_id from category_table

-- Now to apply and use the category table data in the application, do as follows


then you can access the data using the following line
```html
<p> category : {{dta.category_id.c_name}} </p>
```
the overall html template looks like,


```html
<div class="post-grid">
                {% for dta in database %}
                
                <div class="post-card">
                    <img src="{{dta.img_url}}" alt="image">
                    <div class="post-content">
                        <h3>Username : {{dta.username}} </h3>

                        <p> category : {{dta.category_id.c_name}} </p>

                        <a href="{% url 'Notes:Post_detail' slug=dta.slug %}" class="read-more">read-more</a>
                    </div>
                </div>
                {% endfor %}
            </div>
```

now you can see the output in te web page



to update this is in details also,

in 'details.html' 
```html
<h1>{{user_dat.username}}'s details</h1>
            <div class="meta">
                <span class="author">{{user_dat.username}}</span>
                <span class="category">{{ user_dat.category_id.c_name }}</span>
                <span class="date">{{user_dat.created_at }}</span>
            </div>

```


## deleting/recreating tables

if you have done any mistake in themgrations , you can delete it by
* delete the necessary migration files
* in the database table, search and delete the migration data rows
  
  then re run the command to make migrations and migrate


## related posts

to add related category posts

```python
#in views.py

def detail(request,slug):
    related_posts=User_database.objects.filter(category=post.category).exclude(pk=post.id)
    return render(request,'details.html',{'user_dat':user_data,'related_posts':related_posts})

```
in templates
```html
{% for post in related_posts %}
<p>post</p>

{% endfor %}

```

## Pagination 
