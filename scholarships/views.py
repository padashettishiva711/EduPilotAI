#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Scholarship


def scholarship_list(request):

    scholarships = Scholarship.objects.all()

    return render(
        request,
        "scholarships.html",
        {
            "scholarships": scholarships
        }
    )