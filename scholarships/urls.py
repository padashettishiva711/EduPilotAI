from django.urls import path
from .views import scholarship_list

urlpatterns = [
    path(
        '',
        scholarship_list,
        name='scholarships'
    ),
]