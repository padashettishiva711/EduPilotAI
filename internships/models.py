#from django.db import models

# Create your models here.
from django.db import models


class Internship(models.Model):

    title = models.CharField(max_length=255)

    company = models.CharField(max_length=255)

    skills_required = models.TextField()

    description = models.TextField()

    application_url = models.URLField()

    stipend = models.CharField(max_length=100)

    location = models.CharField(max_length=255)

    deadline = models.DateField()

    def __str__(self):
        return self.title



from django.contrib.auth.models import User


class InternshipApplication(models.Model):

    STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('interview', 'Interview'),
        ('selected', 'Selected'),
        ('rejected', 'Rejected'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    internship = models.ForeignKey(
        Internship,
        on_delete=models.CASCADE
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='applied'
    )

    applied_at = models.DateTimeField(
        auto_now_add=True
    )