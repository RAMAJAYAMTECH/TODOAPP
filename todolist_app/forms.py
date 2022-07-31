from django import forms
from django.forms import fields
from todolist_app.models import Tasklist,gst_master,work

class TaskForm(forms.ModelForm):
    class Meta:
       model = Tasklist
       fields = '__all__'

class TaskForm2(forms.ModelForm):
    class Meta:
       model = gst_master
       fields = '__all__'