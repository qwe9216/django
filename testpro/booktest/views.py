from django.shortcuts import render

# Create your views here.

def index(request):
    context = {'hello':'world'}
    return render(request, 'booktest/index.html',context)
