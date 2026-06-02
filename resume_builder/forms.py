from django import forms
from .models import Resume


class ResumeForm(forms.ModelForm):

    class Meta:
        model = Resume

        fields = [
            'full_name',
            'education',
            'skills',
            'projects',
            'experience',
            'career_goal'
        ]