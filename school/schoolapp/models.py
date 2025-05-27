from django.db import models

# Create your models here.

class Teacher(models.Model):
    photo=models.ImageField(upload_to='photo')
    name=models.CharField(max_length=255)
    course=models.CharField(max_length=255)
    description=models.TextField()
    def __str__(self):
        return self.name




class Course(models.Model):
    photo=models.ImageField(upload_to='photo')
    name=models.CharField(max_length=255)
    fee=models.PositiveIntegerField(default=0)
    description=models.TextField()
    def __str__(self):
        return self.name
    
class User(models.Model):
    username=models.CharField(max_length=255)
    password=models.TextField()
    def __str__(self):
        return self.username