from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import StudyPlanForm


@login_required
def create_plan(request):

    plan_text = ""

    if request.method == "POST":

        form = StudyPlanForm(request.POST)

        if form.is_valid():

            study_plan = form.save(commit=False)

            study_plan.user = request.user

            plan_text = f"""
Study Plan

Subjects:
{study_plan.subjects}

Daily Hours:
{study_plan.hours_per_day}

Schedule:

1 Hour - Subject 1

1 Hour - Subject 2

1 Hour - Revision

1 Hour - Practice
"""

            study_plan.generated_plan = plan_text

            study_plan.save()

    else:
        form = StudyPlanForm()

    return render(
        request,
        'study_plan.html',
        {
            'form': form,
            'plan': plan_text
        }
    )