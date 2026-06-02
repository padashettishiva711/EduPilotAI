from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Resume(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    full_name = models.CharField(max_length=200)

    education = models.TextField()

    skills = models.TextField()

    projects = models.TextField()

    experience = models.TextField(
        blank=True
    )

    career_goal = models.TextField()

    generated_resume = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.full_name