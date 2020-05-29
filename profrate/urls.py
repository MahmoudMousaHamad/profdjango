from django.urls import path, include
from .views import index, addSchool, addProf, register, rateSchool, rateProf
urlpatterns = [
    path('', index, name="index"),
    path('add_school', addSchool, name="addSchool"),
    path('rate_school', rateSchool, name="rateSchool"),
    path('add_prof', addProf, name="addProf"),
    path('rate_prof', rateProf, name="rateProf"),
    path('register', register, name="register"),
    path('', include("django.contrib.auth.urls")),
]
