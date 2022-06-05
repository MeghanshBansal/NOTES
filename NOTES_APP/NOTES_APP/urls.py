"""NOTES_APP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from APP.views import all_notes, add_note, delete, setNew, edit

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', all_notes, name='all_notes'),
    path('add_new/', add_note, name="add_note"),
    path('delete/<str:id>/', delete, name='delete'),
    path('setNew/<str:id>/', setNew, name='setNew'),
    path('edit/<str:id>/', edit, name='edit')
]
