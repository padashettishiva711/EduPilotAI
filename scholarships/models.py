from django.db import models

# Create your models here.
from django.db import models


class Scholarship(models.Model):

    title = models.CharField(max_length=255)

    provider = models.CharField(max_length=255)

    description = models.TextField()

    eligibility = models.TextField()

    application_link = models.URLField()

    deadline = models.DateField()

    amount = models.CharField(max_length=100)

    def __str__(self):
        return self.title