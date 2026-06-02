from django import forms
from .models import StudyPlan


class StudyPlanForm(forms.ModelForm):

    class Meta:
        model = StudyPlan

        fields = [
            'exam_date',
            'subjects',
            'hours_per_day'
        ]