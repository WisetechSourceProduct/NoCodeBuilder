from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path("website_editor/", views.website_editor, name="website_editor_page"), # Now it's placed in `about us` page but Need to remove after complete development
    path('save_pages/', views.save_pages, name='save_pages'),
    path('submit-form/', views.handle_form_submission, name='handle_form_submission')
]