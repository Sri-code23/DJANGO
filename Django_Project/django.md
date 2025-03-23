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
