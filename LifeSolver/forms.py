from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

class CustomSignupForm(SignupForm):
    confirm_password = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'})
    )

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        confirm_password = cleaned_data.get("confirm_password")

        if password1 and confirm_password and password1 != confirm_password:
            self.add_error("confirm_password", "Passwords do not match.")

        # Optional: run default Django validators
        if password1:
            validate_password(password1)

        return cleaned_data
