from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello, world. You're at the checklist homepage.")

def checklist(request, year, month, day):
	return HttpResponse("You're checking the daily checklist.")
