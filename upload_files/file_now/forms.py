from django import forms
from .models import fileModel

class fileModelForm(forms.ModelForm):
    class Meta:
        model = fileModel
        fields = "__all__"