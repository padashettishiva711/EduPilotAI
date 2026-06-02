from django.urls import path
from .views import upload_document,document_detail

from .views import (
    upload_document,
    rag_chat
)


urlpatterns = [
    path(
        '',
        upload_document,
        name='learning_hub'
    ),


path(
    'document/<int:document_id>/',
    document_detail,
    name='document_detail'
),

    path(
        'rag-chat/',
        rag_chat,
        name='rag_chat'
    ),


]