from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from openai import OpenAI
from .models import ChatMessage
client = OpenAI(
    api_key=settings.OPENAI_API_KEY
)

@login_required
def chat(request):

    answer = ""

    if request.method == "POST":

        question = request.POST.get("question")

        response = client.responses.create(
            model="gpt-5",
            input=question
        )

        answer = response.output_text

        # Save chat history to database
        ChatMessage.objects.create(
            user=request.user,
            question=question,
            answer=answer
        )

    return render(
        request,
        "chat.html",
        {
            "answer": answer
        }
    )

@login_required
def chat_history(request):

    messages = ChatMessage.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(
        request,
        'chat_history.html',
        {
            'messages': messages
        }
    )