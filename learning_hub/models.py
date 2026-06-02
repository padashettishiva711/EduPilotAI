from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class UploadedDocument(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    title = models.CharField(
        max_length=200
    )

    file = models.FileField(
        upload_to="documents/"
    )

    extracted_text = models.TextField(
        blank=True
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True

    )

class DocumentChunk(models.Model):
    document = models.ForeignKey(
        UploadedDocument,
        on_delete=models.CASCADE,
        related_name='chunks'
        )

    chunk_text = models.TextField()

    chunk_number = models.IntegerField()

    created_at = models.DateTimeField(
            auto_now_add=True
        )