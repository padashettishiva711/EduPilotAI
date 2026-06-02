#rom django.contrib import admin

# Register your models here.
#from django.contrib import admin
#from .models import UploadedDocument

from django.contrib import admin

from .models import (
    UploadedDocument,
    DocumentChunk)

admin.site.register(UploadedDocument)



admin.site.register(DocumentChunk)