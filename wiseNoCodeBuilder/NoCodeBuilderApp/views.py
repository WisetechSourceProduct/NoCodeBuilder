from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, "NoCodeBuilderApp/home.html")

def sample(request): # Need to remove after complete development
    return render(request, "NoCodeBuilderApp/website_editor.html")