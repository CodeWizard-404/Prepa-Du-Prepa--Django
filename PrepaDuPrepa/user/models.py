from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class CustomUser(models.Model):
    user = models.OneToOneField(User,
                                related_name='customUser',
                                on_delete=models.SET_NULL,
                                null=True
                                )
    id = models.AutoField(primary_key=True)
    roles = models.CharField(max_length=7)

    

class course(models.Model):
    courseId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    level = models.IntegerField()

    def __str__(self):
        return self.title
    
class subject(models.Model):
    subjectId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    course = models.ForeignKey(course, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title

class content(models.Model):
    types = [
        ('cours', 'Cours'),
        ('td', 'Travaux Dirigés'),
        ('tp', 'Travaux Pratiques'),
        ('exam', 'Examen'),
    ]

    contentid = models.AutoField(primary_key=True)
    course = models.ForeignKey(course, on_delete=models.CASCADE,null=True)
    subject = models.ForeignKey(subject, on_delete=models.CASCADE,null=True)
    type = models.CharField(max_length=10, choices=types, default='cours')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    document = models.FileField(upload_to='documents/%Y/%m/%d')
    
    
    def __str__(self):
        return self.title