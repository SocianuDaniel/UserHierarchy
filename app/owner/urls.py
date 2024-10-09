""" urls for the owner """
from django.urls import path
from .  import views
app_name = "owner"
urlpatterns = [
    path('register/', views.create_owner, name='create')
]

