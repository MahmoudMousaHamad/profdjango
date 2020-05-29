from django.contrib import admin
from .models import School, Prof, SchoolRating

# Register your models here.
admin.site.register(School)
admin.site.register(Prof)
admin.site.register(SchoolRating)
