from django import forms


class InterviewForm(forms.Form):

    topic = forms.CharField(
        max_length=100
    )

    answer = forms.CharField(
        widget=forms.Textarea
    )