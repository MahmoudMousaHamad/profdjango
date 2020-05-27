from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils.translation import gettext as _
from .forms import RegisterForm, AddSchoolForm, AddProfForm

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
        return render(request, 'register/register.html', context={"title": title, "form": form})


def addSchool(request):
    title = "أضف جامعة"
    if (request.method == 'POST'):
        school = AddSchoolForm(request.POST)

        if school.is_valid():
            school.save()
            return redirect('/')
    elif request.method == 'GET':
        school = AddSchoolForm()
        return render(request, 'school/add-school.html', context={'title': title, 'school': school})


def addProf(request):
    title = "أضف مدرس"
    if (request.method == 'POST'):
        school = AddProfForm(request.POST)

        if school.is_valid():
            school.save()
            return redirect('/')
    elif request.method == 'GET':
        prof = AddProfForm()
        return render(request, 'prof/add-prof.html', context={'title': title, 'form': prof})
