from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def blog1(request):
    return HttpResponse('<p>This is our blog page.</p>')