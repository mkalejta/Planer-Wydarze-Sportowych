import django.views.generic as generic
from django.shortcuts import render
from config import forms
from django.urls import reverse_lazy

class SignUpView(generic.CreateView):
    template_name = 'registration.html'
    form_class = forms.SignUp
    success_url = reverse_lazy('admin')
