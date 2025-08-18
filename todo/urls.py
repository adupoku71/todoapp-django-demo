from django.urls import path
from . import views


app_name = "todo"
urlpatterns = [
    path('', views.all, name="all"),
    path('tasks/', views.all, name="all"),
    path('tasks/<int:id>/', views.detail, name="detail"),
]