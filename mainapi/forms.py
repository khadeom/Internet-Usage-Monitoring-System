from django import forms
from .models import UserData
class UserForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ['username', 'mac_address', 'start_time', 'usage_time', 'upload', 'download']