from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class StudyPlan(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    exam_date = models.DateField()

    subjects = models.TextField()

    hours_per_day = models.IntegerField()

    generated_plan = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user.username} Study Plan"