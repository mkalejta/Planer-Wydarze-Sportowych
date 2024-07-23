import django.forms as f
from django.db.transaction import atomic
from app import models
from django.contrib.auth.forms import UserCreationForm


def CapitalizeValidation(c):
    if c[0].islower():
        raise f.ValidationError(f"{c} musi się zaczynać wielką literą!")


class SignUp(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ('username', 'first_name', 'last_name')

    @atomic
    def save(self, commit=True):
        user = super().save(commit)
        profile = models.Profile(user=user)
        if commit:
            profile.save()
        return user