from django.http import HttpResponse
from django.shortcuts import render, redirect
from myapp.models import *

def home(request):
    return redirect('/home')

def show_about_page(request):
    name = 'Made By Manoj Verma'
    link = 'https://github.com'

    data = {
        'name': name,
        'link': link,
    }

    return render(request, "about.html", data)


def show_home_page(request):
    images = Image.objects.all()
    cats = Category.objects.all()

    data = {'images': images, 'cats': cats}

    return render(request, "home.html", data)


def show_category_page(request, cid):
    cats = Category.objects.all()

    cat = Category.objects.get(pk=cid)

    images = Image.objects.filter(category=cat)
    data = {'images': images, 'cats': cats}

    return render(request, "home.html", data)
