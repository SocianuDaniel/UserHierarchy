""" urls for the owner """
from django.urls import path
from . import views
from django.views.generic.base import TemplateView
app_name = "supervisor"
urlpatterns = [
    
    path('',views.dashboard,name='dashboard')
]
