from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class InterviewSession(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    topic = models.CharField(
        max_length=200
    )

    question = models.TextField()

    student_answer = models.TextField()

    feedback = models.TextField()

    score = models.IntegerField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )