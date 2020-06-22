
from django.shortcuts import render


def home_page(request):
    return render(request, "home_page.html")


def read_more(request):
    return render(request, "read_more.html")




