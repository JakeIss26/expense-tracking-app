# myapp/forms.py
from django import forms
from .models import Expense
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['name', 'amount', 'category', 'date', 'type']
        labels = {
            'name': _("Name"),
            'amount': _("Amount"),
            'category': _("Category"),
            'date': _("Date"),
            'type': _("Type"),
        }


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label=_("Email"))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': _("Username"),
            'email': _("Email"),
            'password1': _("Password"),
            'password2': _("Confirm Password"),
        }


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        labels = {
            'username': _("Username"),
            'email': _("Email"),
        }
