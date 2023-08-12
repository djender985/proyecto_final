from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormTile(forms.Form):    
    titulo = forms.CharField(max_length=150)
    subtitulo = forms.CharField(max_length=100)
    cuerpo = forms.CharField(widget=forms.Textarea)
    imagen = forms.ImageField()