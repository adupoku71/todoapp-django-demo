from django.urls import path
from django.views.generic.base import RedirectView
from . import views


app_name = "todo"
urlpatterns = [
    path('', RedirectView.as_view(url="/tasks/", permanent=True)),
    path('tasks/', views.all, name="all"),
    path('tasks/add/', views.add_task, name="add_task"),
    path('tasks/<int:id>/update/', views.update_task, name="update_task"),
    path('tasks/<int:id>/', views.detail, name="detail"),
]