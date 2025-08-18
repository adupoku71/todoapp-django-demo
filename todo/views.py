from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Task
from .forms import AddTaskForm, TaskForm

# Create your views here.

def all(request):
    tasks = Task.objects.all()
    form = AddTaskForm()
    context = {"tasks": tasks, "form": form}
    return render(request, 'todo/home.html', context)

def add_task(request):
    if request.POST:
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Task added successfully!!!")
        else:
            messages.error(request, "Please correct the errors below")
                
    return redirect('todo:all')
    

def detail(request, id):
    task = Task.objects.get(pk=id)

    return render(request, "todo/detail.html", {"task": task})
    
    
