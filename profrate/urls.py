from django.urls import path, include
from .views import index
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('register', views.register, name="register"),
    path('', include("django.contrib.auth.urls")),
]
