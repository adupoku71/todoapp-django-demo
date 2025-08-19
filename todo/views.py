from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .models import Task
from .forms import TaskForm, AddTaskForm

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


def update_task(request, id):
    task = Task.objects.get(pk=id)
    if request.POST:
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect(reverse('todo:detail', args=[id]))
    else:
        form = TaskForm(instance=task)
    return render(request, "todo/update.html", {"form":form, "id": id, "task":task})


def detail(request, id):
    task = Task.objects.get(pk=id)

    return render(request, "todo/detail.html", {"task": task})
    
    
