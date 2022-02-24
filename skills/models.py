from unicodedata import category
from django.db import models
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

# Create your models here.
CATEGORY = (
    ('VIDEO', 'VIDEO'),
    ('PDF', 'PDF'),
)

class skill(models.Model):
    title = models.CharField(max_length=1000)
    def __str__(self):
        return self.title


class project(models.Model):
    project_name = models.CharField(max_length=1000)
    view_link = models.URLField(null=True, blank=True)
    source_code_link = models.URLField(null=True, blank=True)
    category = models.CharField(max_length=1000, choices=CATEGORY, null=True, blank=True)
    def __str__(self):
        return str(self.project_name).upper()


