from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path("sample/", views.sample, name="samplePage"), # Now it's placed in `about us` page but Need to remove after complete development
    path("editing", views.editing, name="editPage") # Now it's placed in `about us` page but Need to remove after complete development

]