from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Aufgabensammulungen")


def erstellen(request):
	return HttpResponse("Aufgabensammulung erstellen")