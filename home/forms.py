from django import forms
from home.models import TaskModel
class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['taskTitle','taskDescription']