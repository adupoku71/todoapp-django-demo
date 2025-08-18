from django.shortcuts import render
from .models import Task
# Create your views here.

def all(request):
    tasks = Task.objects.all()
    context = {"tasks": tasks}
    return render(request, 'todo/home.html', context)


def detail(request, id):
    task = Task.objects.get(pk=id)

    return render(request, "todo/detail.html", {"task": task})
    
    
