from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from LCS.models import person


class CreateNewUser(UserCreationForm):
    first_name = forms.CharField(label="First Name", max_length=50)
    last_name = forms.CharField(label="Last Name", max_length=50)
    email_address = forms.EmailField(label="Email", max_length=70)
    mobile = forms.IntegerField(label="Phone Number")

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email_address", "password1", "password2", "mobile")
