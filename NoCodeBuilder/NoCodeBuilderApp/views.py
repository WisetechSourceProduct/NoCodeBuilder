from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    print("Check")
    return HttpResponse("Hello World")