from django.urls import path, include
from .views import index, addSchool, addProf, register
urlpatterns = [
    path('', index, name="index"),
    path('add_school', addSchool, name="addSchool"),
    path('add_prof', addProf, name="addProf"),
    path('register', register, name="register"),
    path('', include("django.contrib.auth.urls")),
]
