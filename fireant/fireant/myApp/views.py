from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'myApp/main.html')

def sub1(request):
    return render(request, 'myApp/sub1.html')

def sub2(request):
    return render(request, 'myApp/sub2.html')