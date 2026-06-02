from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class CareerRecommendation(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    career_name = models.CharField(max_length=200)

    score = models.IntegerField()

    roadmap = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.career_name