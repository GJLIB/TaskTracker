from django import forms
from .models import Task, Coment # Припустимо, у вас є модель Task

class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}), required=False)
    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline', 'status', 'priority'] # Поля для форми

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'clas': 'form-control'})

class ComentForm(forms.ModelForm):
    class Meta:
        model = Coment
        fields = ['content', 'media']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})