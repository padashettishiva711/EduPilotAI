from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from student_profile.models import StudentProfile


@login_required
def generate_roadmap(request):

    profile = StudentProfile.objects.get(
        user=request.user
    )

    roadmap = f"""
Career Goal: {profile.career_goal}

Step 1:
Learn Python

Step 2:
Learn Mathematics

Step 3:
Learn Machine Learning

Step 4:
Learn Deep Learning

Step 5:
Build Projects

Step 6:
Internships

Step 7:
Interview Preparation

Step 8:
Job Applications
"""

    return render(
        request,
        "roadmap.html",
        {
            "roadmap": roadmap
        }
    )