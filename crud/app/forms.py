from django import forms
from .models import appTask

class TaskForm(forms.ModelForm):
    class Meta:
        model = appTask
        fields = "__all__"
        