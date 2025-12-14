from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import*
from .models import Task, Coment
from .forms import*
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import AuthorRequiredMixin
from django.shortcuts import redirect
class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'task_list'
    ordering = ['-created_at', '-priority']
    def get_queryset(self):
        tasks = Task.objects.filter(author=self.request.user)
        status = self.request.GET.get('status')
        if status:
            tasks = tasks.filter(status = status)
        return tasks
class TaskDetailView(AuthorRequiredMixin, DetailView):
    model = Task
    template_name = 'task_detail.html'
    content_object_name = 'task'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = ComentForm()
        return context
    
    def post(self, request, *args, **kwargs):
        task = self.get_object
        form = ComentForm(request.POST, request.FILES)
        if form.is_valid():
            coment = form.save(commit = False)
            coment.author = request.user
            coment.task = task
            coment.save()
            return redirect('task_detail' , pk =task.pk)


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('home')

    def  form_valid(self, form):
         form.instance.author = self.request.user
         form.save()
         return super().form_valid(form)
    
class TaskUpdateView(AuthorRequiredMixin, UpdateView):
    model  = Task
    form_class = TaskForm
    template_name = 'task_update.html'
    success_url = reverse_lazy('home')

class TaskDeleteView(AuthorRequiredMixin, DeleteView):
    model = Task
    template_name = 'task_delete.html'
    success_url = reverse_lazy('home')