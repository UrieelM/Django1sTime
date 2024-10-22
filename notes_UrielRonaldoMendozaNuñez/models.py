from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    title_note = models.CharField(max_length=50)
    content_note = models.CharField(max_length=500)
    creation_date_note = models.DateTimeField("Fecha de creación de la nota", auto_now_add=True)

    def __str__(self):
        return self.title_note
