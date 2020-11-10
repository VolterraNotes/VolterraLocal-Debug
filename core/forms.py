from django.contrib.auth.forms import UserCreationForm
from django import forms
from content.models import Classe
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("classe", "email", "profile_image")
