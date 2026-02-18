from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Choice, Question


def index(request):
    return HttpResponse("Hello, this is polls home page")


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return HttpResponse(f"You are viewing question {question_id}")


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return HttpResponse(f"Results for question {question_id}")


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return HttpResponse("You didn't select a choice.")
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()

        return HttpResponseRedirect(
            reverse("polls:results", args=(question.id,))
        )
