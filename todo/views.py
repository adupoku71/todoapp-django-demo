from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
# Create your views here.

def all(request):
    tasks = Task.objects.all()
    page = ""
    for task in tasks:
        page += f"<a href={task.pk}> {task.title}<a/> - {task.description} - {'Done' if task.completed else 'Not Done'} <br/>"
    return HttpResponse(page)


def detail(request, id):
    task = Task.objects.get(pk=id)
    page = f"""{task.title} - <input type=checkbox {"checked" if task.completed else ""}/> <br/> 
               {task.description}
            """
    return HttpResponse(page)
    
    
