from django.shortcuts import render

def page_open(request):
    return render (request, 'index.html')
# Create your views here.
