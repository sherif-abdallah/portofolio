from django.contrib import admin
from .models import skill, project

# Register your models here.
admin.site.site_header = 'Sherif Abdullah'

admin.site.register(skill)
admin.site.register(project)