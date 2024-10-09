# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from core.models import Owner

def create_owner(request):
    return render(request, 'owner/register.html')
