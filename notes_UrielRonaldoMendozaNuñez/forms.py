from django import forms
from .models import Note
from django.contrib.auth.models import User

class NoteForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all(), label="Usuario")  # Campo para seleccionar el usuario

    class Meta:
        model = Note
        fields = ['user', 'title_note', 'content_note']  # Incluye el campo 'user' en el formulario
