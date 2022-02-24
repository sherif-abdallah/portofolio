from django.shortcuts import render
from .models import skill, project
# Create your views here.
def Home_views(request):
    skills_object = skill.objects.all()
    project_object = project.objects.all()
    return render(request, 'index.html', {'skills': skills_object, 'projects':project_object})