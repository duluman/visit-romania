
from django.shortcuts import render


def homepage(request):

    custom_list = [{
        "id": 1,
        "name": "Hotel 1"},
        {
            "id": 2,
            "name": "Hotel 2"},
        {
            "id": 3,
            "name": "Hotel 3"},
    ]

    homepage_context = {
        "title": "This is my homepage",
        "custom_list": custom_list
    }
    return render(request, "homepage.html", homepage_context)

