from django import forms
from .models import UserInfo

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['first_name', 'last_name', 'profile_images','bio', 'specialization', 'contact_email', 'phone', 'profile_images', 'available_for_consultation', 'birth_date', 'city']

