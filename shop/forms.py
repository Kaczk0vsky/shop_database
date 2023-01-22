from django import forms
from .models import Users


class NewUser(forms.ModelForm):
    class Meta:
        model = Users
        fields = [
            "id",
            "username",
            "password",
            "e_mail",
            "created_at",
        ]
        labels = {
            "id": "ID",
            "username": "Username",
            "password": "Password",
            "e_mail": "Email",
            "created_at": "Created_at",
        }
