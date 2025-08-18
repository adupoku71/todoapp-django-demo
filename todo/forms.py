from django import forms
from .models import Task


class AddTaskForm(forms.Form):
    title = forms.CharField(max_length=200, label="")
    

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title"]