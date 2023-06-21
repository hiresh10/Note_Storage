from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class UserMaster(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)

    

class Note(models.Model):
    NOTE_TYPES = [
        ('text', 'Text'),
        ('audio', 'Audio'),
        ('video', 'Video'),
    ]

    type = models.CharField(max_length=10, choices=NOTE_TYPES)
    content = models.TextField()
    name = models.CharField(max_length=100)
    note_file = models.FileField(upload_to='app/note_files', null=True, blank=True)

    def __str__(self):
        return f"{self.type} Note by {self.name}"
    



