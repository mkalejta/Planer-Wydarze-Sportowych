import django.views.generic as generic
from config import forms
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.contrib.messages.views import messages, SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from app import models


class SignUpView(SuccessMessageMixin, generic.CreateView):
    template_name = 'registration.html'
    form_class = forms.SignUpForm
    success_url = reverse_lazy('admin')
    success_message = "User has been created"

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Please enter details properly")
        return redirect('/accounts/sign_up')


class ProfileView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'profile.html'
    model = models.Profile


class UserDashboard(generic.TemplateView):
    template_name = 'dashboard.html'


def update_profile(request):
    msg = None
    if request.method == 'POST':
        form = forms.UpdateProfile(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            msg = 'Data has been saved'
    form = forms.UpdateProfile(instance=request.user)
    args = {'form': form, 'msg': msg}
    return render(request, 'update_profile.html', args)