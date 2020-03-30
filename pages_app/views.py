from django.shortcuts import render
from django.http import HttpResponse

def homeView(request):
    return HttpResponse('<h1> Hello world </h1>')


def aboutView(request):
    names=['John','Rachel','Peter','Samanda']
    return render(request, 'pages_app/about.html',{'names':names})


