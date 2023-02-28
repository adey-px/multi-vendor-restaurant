from django import forms
from .models import User


class registerForm(forms.ModelForm):
    """
    Create form fields from selected fields in custom
    User model. Fields here used as input elements
    in registerUser template via views.py
    """

    # add custom pword fields not listed in User model
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

    # custom fields validation
    def clean(self):
        """
        Validate password fields and catch any
        non-field erros. Both field & non-field
        errors show in registerUser template.
        Field errors are handled in views.
        """

        # this shows as non_field_errors in template
        cleaned_data = super(registerForm, self).clean()
        password = cleaned_data.get('password')
        conf_password = cleaned_data.get('conf_password')

        if password != conf_password:
            raise forms.ValidationError(
                'Passwords do not match'
            )