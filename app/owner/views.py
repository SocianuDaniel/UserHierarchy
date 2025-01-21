# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
# from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from core import models
from django.contrib.auth.decorators import login_required

# from core.models import Owner
from core import forms


def register_owner(request):
    if request.method == "POST":
        form = forms.CreateNewUserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            user = get_user_model().objects.create_user(
                email=email, password=password1
                )
            if user:
                owner = models.Owner()
                owner.user = user
                owner.level = 1
                owner.save()
                return redirect('owner:registration-complete')

        return render(request, 'owner/register.html', {'form': form})
    else:
        form = forms.CreateNewUserForm()
        return render(request, 'owner/register.html', {'form': form})

@login_required
def supervisor_create(request):
    if request.method == "POST":
        form = forms.CreateNewUserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            owner = get_object_or_404(models.Owner, user=request.user)
            
            user = get_user_model().objects.create_user(
                email=email, password=password1
                )
            if user:
                supervisor = models.Supervisor()
                supervisor.user = user
                supervisor.level = 2
                supervisor.owner = owner
                supervisor.save()
                return redirect('owner:registration-complete')

        return render(request, 'owner/dash/supervisor/create.html', {'form': form})
    else:
        form = forms.CreateNewUserForm()
        return render(request, 'owner/dash/supervisor/create.html', {'form': form})
    


@login_required
def dashboard(request):
    return render(request, 'owner/dash/dashboard.html')
