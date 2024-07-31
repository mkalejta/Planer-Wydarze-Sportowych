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
    first_name = f.CharField(max_length=150, validators=[CapitalizeValidation])
    last_name = f.CharField(max_length=150, validators=[CapitalizeValidation])
    email = f.EmailField(max_length=150)
    birth_date = f.DateField(label="Birth Date",
                             required=True,
                             widget=f.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
                             input_formats=["%Y-%m-%d"])
    password1 = f.CharField(widget=f.PasswordInput)
    password2 = f.CharField(widget=f.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    @atomic
    def save(self, commit=True):
        user = super().save(commit)
        profile = models.Profile(user=user)
        if commit:
            profile.save()
        return user