from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import StudentProfileForm


@login_required
def create_profile(request):

    if request.method == 'POST':

        form = StudentProfileForm(request.POST)

        if form.is_valid():

            profile = form.save(commit=False)

            profile.user = request.user

            profile.save()

            return redirect('dashboard')

    else:
        form = StudentProfileForm()

    return render(
        request,
        'profile_form.html',
        {'form': form}
    )