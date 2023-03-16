from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mlearning(request):
    course = 'machine learning'
    TClass = 21
    seat = 20
    duration = '2.5 months'
    offering = {'c' : course, 'tc' : TClass, 'st' : seat, 'cd' : duration}
    Teachers = {'names' : ['Shakil', 'Mejba', 'Sohanur']}
    return render(request, 'machine_learning/machine_learning.html', context=Teachers)

def random(request):
    return render(request, 'machine_learning/random_forest.html')

def dtree(request):
    return render(request, 'machine_learning/DT.html')

def k_nearest(request):
    return render(request, 'machine_learning/knn.html')