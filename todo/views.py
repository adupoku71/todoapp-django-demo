from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
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
        post_data = request.POST.copy()
        
        if not post_data.get("title"):
            post_data["title"] = task.title
        if not post_data.get("description"):
            post_data["description"] = task.description

        form = TaskForm(post_data, instance=task)
        if form.is_valid():
            print(f'task is {task}')
            form.save()
        return redirect('todo:all')
    else:
        form = TaskForm(instance=task)
    return render(request, "todo/update.html", {"form":form, "id": id, "task":task})


@require_POST
def delete_task(request, id):
    task = Task.objects.get(pk=id)
    task.delete()
    return redirect('todo:all')


def detail(request, id):
    task = Task.objects.get(pk=id)

    return render(request, "todo/detail.html", {"task": task})
    
    
