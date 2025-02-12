import django.views.generic as generic
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.urls import reverse_lazy

from config import forms
from django.shortcuts import redirect, render
from django.contrib.messages.views import messages
from app import models

def SignUpView(request):
    form = forms.SignUpForm()
    if request.method == "POST":
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)

            messages.success(request, ("You have successfully registered!"))
            return redirect('home')

    return render(request, "registration/registration.html", {'form': form})

class UserDashboard(generic.TemplateView):
    template_name = 'dashboard.html'


def logout_user(request):
    logout(request)
    return redirect('home')

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = forms.UpdateProfile(request.POST, request.FILES, instance=request.user)
        profile_form = forms.ProfilePicForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            messages.success(request, "Your profile was successfully updated")
            return redirect('user_dashboard')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = forms.UpdateProfile(instance=request.user)
        profile_form = forms.ProfilePicForm(instance=request.user.profile)
    return render(request, 'update_profile.html', {'user_form': user_form, 'profile_form': profile_form})


def events_list(request):
    qs = models.Event.objects.all()
    sport_category_query = request.GET.get('sport_category')
    print(sport_category_query)
    if sport_category_query != "" and sport_category_query is not None:
        qs = qs.filter(facility__sport__id=sport_category_query)
    context = {
        'queryset': qs
    }
    return render(request, "events_list.html", context)


@login_required
def create_event(request):
    form = forms.CreateEventForm
    if request.method == 'POST':
        form = forms.CreateEventForm(request.POST)
        if form.is_valid():
            new_event = form.save(commit=False)
            new_event.organizer = request.user
            new_event.save()
            return redirect('events_list')
    return render(request, "create_event.html", {'form': form})