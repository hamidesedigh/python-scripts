# 🧩 Django Sample Project — `myFirstPage`

This project is a simple demonstration of how to create, configure, and run a **Django web application** from scratch.  
It includes two sample apps — `blog` and `mainpage`.

---

## 🛠️ Steps to Set Up the Project

### 1. Create a project directory

```bash
mkdir myFirstPage
cd myFirstPage
```
### 2. Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate        # On Windows
```
### 3. Install Django

```bash
pip install django
```

### 4. Create a Django project

```bash
django-admin startproject myFirstPage
cd myFirstPage
```
### 5.1 Create Django apps

```bash
python manage.py startapp blog
python manage.py startapp mainpage
```
🧱 Configure the blog App
Add `urls.py` inside the `blog` directory:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```
Edit `views.py` in the `blog` directory:
```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the blog page.")
```
Update the main `urls.py` in the `myFirstPage` directory:
```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the blog page.")
```
Update the main `urls.py` in the `myFirstPage` directory:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('mainpage/', include('mainpage.urls')),
]
```
### 5.2 Register the App in `settings.py`
In `myFirstPage/settings.py`, add both apps to the `INSTALLED_APPS` list:
```python
INSTALLED_APPS = [
    'blog.apps.BlogConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles'
]
```
Create a Simple Django Model
Edit `blog/models.py`
```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```
Register your model in `blog/admin.py`
```python
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```
Add to `blog/view.py`
``` python
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
# Create your views here.

def index(request):
    ret = '<body>'
    all_posts = Post.objects.all()
    for post in all_posts:
       ret = ret + '<p>' + post.text + '</p>'
    ret = ret + '</body>'
    return HttpResponse(ret)
```

Apply Migrations
```bash
python manage.py makemigrations blog
python manage.py migrate
```
Create a Superuser (Admin Account)
```bash
python manage.py createsuperuser
```
### 6. Run the development server
```bash
python manage.py runserver
```
Then open your browser and visit: 

http://127.0.0.1:8000/blog/
 → Blog app

http://127.0.0.1:8000/admin/
 → Admin panel
👤 Author

Hamideh Sedigh
Created on Tuesday, November 14, 2025