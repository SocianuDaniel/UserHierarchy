# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from core import models


from core.models import Owner
from core import forms
def register_owner(request):
    if request.method == "POST":
        form  = forms.CreateOwnerForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            print("email=", email)
            password1 = form.cleaned_data['password1']
            user = get_user_model().objects.create_user(email=email, password=password1)
            if user:
                owner = models.Owner()
                owner.user = user
                owner.level = 1
                owner.save()
                return redirect('owner:registration-complete')
            
        return render(request, 'owner/register.html',{'form': form})
    else:
        form = forms.CreateOwnerForm()
        return render(request, 'owner/register.html',{'form': form})
