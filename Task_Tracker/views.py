from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import*
from .models import Task
from .forms import*
class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'task_list'
    ordering = ['-created_at'] # Сортування за датою публікації (від нових до старих)

class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'
    content_object_name = 'task'

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('home')

    def  form_valid(self, form):
         form.instance.author = self.request.user
         form.save()
         return super().form_valid(form)
    
class TaskUpdateView(UpdateView):
    model  = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    succes_url = reverse_lazy('home')