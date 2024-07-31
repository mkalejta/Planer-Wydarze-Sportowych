import django.views.generic as generic
from config import forms
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.messages.views import messages, SuccessMessageMixin


class SignUpView(SuccessMessageMixin, generic.CreateView):
    template_name = 'registration.html'
    form_class = forms.SignUpForm
    success_url = reverse_lazy('admin')
    success_message = "User has been created"

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Please enter details properly")
        return redirect('https://www.google.com/?hl=pl')
