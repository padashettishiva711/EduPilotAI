from django.urls import path
from .views import career_guidance

urlpatterns = [
    path(
        '',
        career_guidance,
        name='career_guidance'
    ),
]