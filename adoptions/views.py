from django.shortcuts import render
from django.http import HttpResponse, Http404
from adoptions.models import Pet

# Create your views here.


def pet_view(request):
    pets = Pet.objects.all()
    return render(request, "adoptions/pets.html", {'pets': pets})


def pet_details(request, pet_id):
    # pet = Pet.objects.filter(id=pet_id)
    try:
        pet_obj = Pet.objects.get(id=pet_id)
    except Pet.DoesNotExist:
        raise Http404('pet not found')

    return render(request, "adoptions/pet_details.html", {'pet': pet_obj})


def pet_test_variable_view(request):
    return HttpResponse('This is a dummy page')
