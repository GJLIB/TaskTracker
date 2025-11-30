from django.shortcuts import render

from django.views.generic import*
from .models import Task # Припустимо, у вас є модель Post

class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'task_list'
    ordering = ['-created_at'] # Сортування за датою публікації (від нових до старих)

class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'
    content_object_name = 'task'
