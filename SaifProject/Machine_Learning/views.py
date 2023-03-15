from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mlearning(request):
    return render(request, 'machine_learning/machine_learning.html')

def dtree(request):
    return render(request, 'machine_learning/DT.html')

def random(request):
    return render(request, 'machine_learning/random_forest.html')

def k_nearest(request):
    return render(request, 'machine_learning/knn.html')