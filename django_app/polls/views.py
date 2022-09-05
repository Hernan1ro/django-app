from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("Estás en la página principal de premios platiz app")


def detail(request, question_id):
    return HttpResponse(f"Estás viend la pregunta número {question_id}")


def results(request, question_id):
    return HttpResponse(f"Estas viendo los resultados de la pregunto número {question_id}")


def vote(request, question_id):
    return HttpResponse(f"Estás votando a la pregunta número {question_id}")