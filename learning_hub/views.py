#from django.shortcuts import render

# Create your views here.

from django.contrib.auth.decorators import login_required

from .forms import DocumentUploadForm


#from .utils import extract_pdf_text

from .models import (

    DocumentChunk
)

from .utils import (
    extract_pdf_text,
    chunk_text
)


from openai import OpenAI
from django.conf import settings

client = OpenAI(
    api_key=settings.OPENAI_API_KEY
)




from django.shortcuts import render
from .embeddings import get_embedding
from .vector_store import collection



@login_required
def upload_document(request):

    if request.method == "POST":

        form = DocumentUploadForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            document = form.save(commit=False)

            document.user = request.user

            document.save()

            pdf_text = extract_pdf_text(
                document.file.path
            )

            document.extracted_text = pdf_text

            document.save()

            chunks = chunk_text(pdf_text)

            for index, chunk in enumerate(chunks):
                # Save chunk in Django DB
                DocumentChunk.objects.create(
                    document=document,
                    chunk_text=chunk,
                    chunk_number=index
                )

                # Generate embedding
                embedding = get_embedding(chunk)

                # Store in ChromaDB
                collection.add(
                    ids=[f"{document.id}_{index}"],
                    embeddings=[embedding],
                    documents=[chunk]
                )



    else:
        form = DocumentUploadForm()

    return render(
        request,
        "upload_document.html",
        {"form": form}
    )



from .models import UploadedDocument


@login_required
def document_detail(
    request,
    document_id
):

    document = UploadedDocument.objects.get(
        id=document_id,
        user=request.user
    )

    return render(
        request,
        "document_detail.html",
        {
            "document": document
        }
    )


def rag_chat(request):

    answer = ""

    if request.method == "POST":

        question = request.POST.get("question")

        query_embedding = get_embedding(
            question
        )

        results = collection.query(
            query_embeddings=[
                query_embedding
            ],
            n_results=5
        )

        retrieved_chunks = "\n".join(
            results["documents"][0]
        )

    prompt = f"""
       You are EduPilot AI.

       Answer ONLY using the context below.

       Context:
       {retrieved_chunks}

       Question:
       {question}

       If the answer is not in the context,
       say:
       'I could not find that information in the uploaded documents.'
       """

    response = client.responses.create(
        model="gpt-5",
        input=prompt
    )

    answer = response.output_text



    return render(
        request,
        "rag_chat.html",
        {
            "answer": answer
        }
    )