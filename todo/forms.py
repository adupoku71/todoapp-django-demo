from django import forms
from .models import Task


class AddTaskForm(forms.Form):
    title = forms.CharField(max_length=200, label="")
    

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make fields conditionally required
        self.fields['title'].required = False
        self.fields['description'].required = False
        

class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"