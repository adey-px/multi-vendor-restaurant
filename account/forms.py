from django import forms
from .models import User


class registerForm(forms.ModelForm):
    """
    Create form fields from selected fields in custom
    User model. Fields here used as input elements
    in registerUser template via views.py
    """

    # add pword fields not listed in User model
    password = forms.CharField(widget=forms.PasswordInput())
    conf_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
        ]
