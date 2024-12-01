from email.mime import audio
from pyexpat import model
from turtle import mode
from django.db import models
from numpy import imag

# Create your models here.


class Song(models.Model):
    title = models.TextField(max_length=100)
    artist = models.TextField(max_length=100)
    image = models.ImageField(upload_to='images')
    audio_file= models.FileField(upload_to='audio')
    audio_link = models.CharField(max_length=200, blank=True, null=True)
    duration = models.CharField(max_length=20)  
    lyrics= models.TextField()
    paginate_by = 2
    

    def __str__(self):
        return self.title