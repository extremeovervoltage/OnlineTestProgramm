from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<html><body><h1>OnlineTestProgramm</h1><div>Mainpage</body></html>")


def erstellen(request):
	return HttpResponse("Aufgabensammulung erstellen")

def frage_ansehen(request, frage_id):
	return HttpResponse("Frage: %s" % frage_id)