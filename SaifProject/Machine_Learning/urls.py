from django.urls import path
from . import views

urlpatterns = [

    path('machine/', views.ml),
    path('dl/', views.dl),
    path('about/', views.about_us),
]
