from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email = forms.EmailField(required=False)

    def clean_username(self):
        username = self.cleaned_data['username']
        users = User.objects.filter(user__username=username)
        import random
        if len(users) >= 1:
            raise ValidationError('this username has taken!')
        return None