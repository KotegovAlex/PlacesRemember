from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .models import Place


class AddPlaceForm(forms.ModelForm):
    """Form to add new place"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    lat = forms.FloatField(label="", widget=forms.HiddenInput(), required=False)
    lon = forms.FloatField(label="", widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Place
        fields = ["title", "content", "photo", "lat", "lon"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-input"}),
            "content": forms.Textarea(attrs={"cols": 60, "rows": 10}),
        }


class RegisterUserForm(UserCreationForm):
    """New user registration form"""

    username = forms.CharField(
        label="Login", widget=forms.TextInput(attrs={"class": "form-input"})
    )
    password1 = forms.CharField(
        label="Password", widget=forms.PasswordInput(attrs={"class": "form-input"})
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={"class": "form-input"}),
    )

    class Meta:
        model = User
        fields = ("username", "password1", "password2")


class LoginUserForm(AuthenticationForm):
    """User authorization form"""

    username = forms.CharField(
        label="Login", widget=forms.TextInput(attrs={"class": "form-input"})
    )
    password = forms.CharField(
        label="Password", widget=forms.PasswordInput(attrs={"class": "form-input"})
    )
