from django.urls import path
from .views import create_resume

urlpatterns = [
    path(
        '',
        create_resume,
        name='resume_builder'
    ),
]