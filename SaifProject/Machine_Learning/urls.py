from django.urls import path
from . import views

urlpatterns = [
    path('machine/', views.mlearning),
    path('dt/', views.dtree), 
    path('rn/', views.random),
    path('knn/', views.k_nearest),
]
