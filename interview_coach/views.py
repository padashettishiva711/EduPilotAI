from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import InterviewForm


@login_required
def interview(request):

    question = "What is Django ORM?"

    feedback = ""

    score = ""

    if request.method == "POST":

        form = InterviewForm(request.POST)

        if form.is_valid():

            answer = form.cleaned_data["answer"]

            if "database" in answer.lower():

                score = 8

                feedback = """
Good answer.
You understand the purpose of ORM.
"""

            else:

                score = 4

                feedback = """
Try explaining how ORM
connects Python models
to databases.
"""

    else:
        form = InterviewForm()

    return render(
        request,
        "interview.html",
        {
            "form": form,
            "question": question,
            "feedback": feedback,
            "score": score
        }
    )