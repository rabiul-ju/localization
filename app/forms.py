from django import forms


class LoginFrom(forms.Form):
    email = forms.EmailField(max_length=255)
    password = forms.CharField(min_length=6)


class RegistrationForm(forms.Form):
    email = forms.EmailField(max_length=255, required=True)
    password = forms.CharField(min_length=6, required=True)
    code = forms.CharField(max_length=255, min_length=15, required=True)
    agreement = forms.BooleanField(required=True)
