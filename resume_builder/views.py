from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import ResumeForm


@login_required
def create_resume(request):

    generated_resume = ""

    if request.method == "POST":

        form = ResumeForm(request.POST)

        if form.is_valid():

            resume = form.save(commit=False)

            resume.user = request.user

            generated_resume = f"""
{resume.full_name}

CAREER OBJECTIVE
{resume.career_goal}

EDUCATION
{resume.education}

SKILLS
{resume.skills}

PROJECTS
{resume.projects}

EXPERIENCE
{resume.experience}
"""

            resume.generated_resume = generated_resume

            resume.save()

    else:
        form = ResumeForm()

    return render(
        request,
        'resume.html',
        {
            'form': form,
            'resume': generated_resume
        }
    )