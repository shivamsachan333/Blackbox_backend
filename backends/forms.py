from django import forms
from .models import ProgramDetail

class ProgramDetailForm(forms.ModelForm):
    class Meta:
        model = ProgramDetail
        fields = ['title', 'subtitle', 'description']