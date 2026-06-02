from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from student_profile.models import StudentProfile


def career_guidance(request):

    profile = StudentProfile.objects.get(
        user=request.user
    )

    career = "AI Engineer"

    score = 95

    roadmap = """
1. Learn Python
2. Learn Mathematics
3. Machine Learning
4. Deep Learning
5. Build Projects
6. Internship
7. Job
"""

    context = {
        "career": career,
        "score": score,
        "roadmap": roadmap
    }

    return render(
        request,
        "career.html",
        context
    )