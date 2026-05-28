from django.urls import path
from . import views

urlpatterns = [
    path("theses/", views.theses, name='theses'),
    path("login/wahlomat/evaluate", views.evaluate, name='evaluate'), 

]