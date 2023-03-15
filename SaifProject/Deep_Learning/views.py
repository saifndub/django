from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def deep_learning(request):
    return render(request, 'deep_learning/deep_learning.html')