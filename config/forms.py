import django.forms as f
from django.db.transaction import atomic
from app import models
from django.contrib.auth.forms import User, UserCreationForm

def CapitalizeValidation(c):
    if c[0].islower():
        raise f.ValidationError(f"{c} musi się zaczynać wielką literą!")


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your username'
        })

        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your first name'
        })

        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your last name'
        })

        self.fields['birth_date'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your birth_date (dd/mm/yyyy)'
        })

        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your email'
        })

        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your password'
        })

        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirm your password'
        })

    username = f.CharField(max_length=30)
    first_name = f.CharField(max_length=150)
    last_name = f.CharField(max_length=150)
    email = f.CharField(max_length=150)
    birth_date = f.DateField()
    password1 = f.CharField(widget=f.PasswordInput)
    password2 = f.CharField(widget=f.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    @atomic
    def save(self, commit=True):
        result = super().save(commit)
        profile = models.Profile(user=result)
        if commit:
            profile.save()
        return result