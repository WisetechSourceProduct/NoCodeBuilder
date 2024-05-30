from django import forms
from .models import FormSubmission

class DynamicForm(forms.ModelForm):
    class Meta:
        model = FormSubmission
        fields = ['form_data']