from django.urls import path
from .views import study_buddy

urlpatterns = [
    path('', study_buddy, name='study_buddy'),
]