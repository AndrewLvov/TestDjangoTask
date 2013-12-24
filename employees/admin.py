from django.contrib import admin

from .models import Employee, Department

admin.site.register(Employee, search_fields=['first_name', 'last_name'])
admin.site.register(Department, search_fields=['name'])
