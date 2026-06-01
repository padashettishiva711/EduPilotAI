

from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    full_name = models.CharField(max_length=100)

    age = models.IntegerField()

    education_level = models.CharField(max_length=100)

    interests = models.TextField()

    skills = models.TextField()

    career_goal = models.CharField(max_length=200)

    def __str__(self):
        return self.full_name