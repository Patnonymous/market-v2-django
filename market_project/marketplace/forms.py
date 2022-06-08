# Imports.
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


# Create custom forms here.
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name')


class CustomUserChangeForm(UserChangeForm):
    """
    CustomUserChangeForm for changing user details on the admin page.
    """
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name')


class EditAccountDetailsForm(forms.ModelForm):
    email = forms.EmailField(label='New Email', required=True)
    first_name = forms.CharField(label='First Name', required=True)
    last_name = forms.CharField(label='Last Name', required=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')
