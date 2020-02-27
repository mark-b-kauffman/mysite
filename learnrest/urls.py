from django.urls import path
from . import views

urlpatterns = [
    path('', views.systemversion, name='systemversion'),
]
