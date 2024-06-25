from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Pages, FormSubmission
from .forms import DynamicForm
import json


# Create your views here.
def home(request):
    return render(request, "NoCodeBuilderApp/home.html")
    #home

def website_editor(request):
    return render(request, "NoCodeBuilderApp/website_editor.html")

@csrf_exempt
def save_pages(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            pages_data = data.get('pages', [])

            # Update existing pages and create new pages
            for page_data in pages_data:
                page_id = page_data['id']
                name = page_data['name']
                html = page_data['html']
                css = page_data['css']
                Pages.objects.update_or_create(id=page_id, defaults={"name":name, "html":html, "css":css, "description":"no desc"})
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})


def handle_form_submission(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            FormSubmission.objects.create(form_data=data)
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})


