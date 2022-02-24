from django.contrib import admin
from django.urls import path
from skills.views import Home_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home_views, name='home')
]
