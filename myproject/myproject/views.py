from django.shortcuts import render

def Homepage(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')