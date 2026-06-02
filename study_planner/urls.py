from django.urls import path
from .views import create_plan

urlpatterns = [
    path(
        '',
        create_plan,
        name='study_plan'
    ),
]