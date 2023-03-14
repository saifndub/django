from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ml(request):
    return render(request, 'machine_learning.html')

def dl(request):
    return HttpResponse('This is deep learning')

def about_us(request):
    return HttpResponse('We have available lots of experience')