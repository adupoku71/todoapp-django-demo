from django.contrib import admin
from .models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "completed", "created_at", "updated_at", "description")
    list_editable = ("completed",)


admin.site.register(Task, TaskAdmin)
