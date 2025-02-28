from django.contrib import admin
from .models import Class, Subject, Faculty, Weekday

# Register your models here.
admin.site.register(Class)
admin.site.register(Subject)
admin.site.register(Faculty)
admin.site.register(Weekday)