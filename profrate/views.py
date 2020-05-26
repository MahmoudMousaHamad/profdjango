from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    title = ""
    return render(request, 'index/index.html', context={"title": title})
