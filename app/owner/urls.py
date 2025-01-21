""" urls for the owner """
from django.urls import path
from . import views
from django.views.generic.base import TemplateView
app_name = "owner"
urlpatterns = [
    path('register/', views.register_owner, name='create'),
    path('thanks/',
         TemplateView.as_view(
             template_name="owner/registration_complete.html"),
         name="registration-complete"),
    
]
urlpatterns += [
    path('',views.dashboard,name='dash-owner'),
        path('dash/supervisor/create/',
         views.supervisor_create,
         name='supervisor-create'
         ),
    
]
