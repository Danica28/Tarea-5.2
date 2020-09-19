"""HOME Test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from .views import HomeView,EstudiantesView,AdministradoresView,InformacionView

urlpatterns = [
    path('index/', HomeView.as_view(), name='home'),
    path('estudiantes/', EstudiantesView.as_view(), name='estudiantes'),
    path('administradores/', AdministradoresView.as_view(), name='administradores'),
    path('informacion/', InformacionView.as_view(), name='informacion'),
]
