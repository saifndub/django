from django.urls import path
from . import views

urlpatterns = [
    path('dlearn',views.deep_learning),
]
