from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils.translation import gettext as _
from .forms import RegisterForm

# Create your views here.


def index(request):
    title = ""
    return render(request, 'index/index.html', context={"title": title})

def register(request):
    title = _("Register")
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("form.is_valid(): ")
            print(form.is_valid())
        return redirect("/")
    else:
        form = RegisterForm()
        return render(request, 'register/register.html', context={"title":title, "form":form})