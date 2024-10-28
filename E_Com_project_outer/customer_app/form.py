from django import forms
from .models import custom_user
class UserAddForm(forms.ModelForm):
    class Meta:
        model = custom_user
        fields = '__all__'
        