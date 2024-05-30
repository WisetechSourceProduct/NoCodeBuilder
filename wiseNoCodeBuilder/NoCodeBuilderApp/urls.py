from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path("sample/", views.sample, name="samplePage"), # Now it's placed in `about us` page but Need to remove after complete development
    path("editing/", views.editing, name="editPage"),
    path('save_pages/', views.save_pages, name='save_pages'),
    path('submit-form/', views.handle_form_submission, name='handle_form_submission')
]