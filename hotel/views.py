from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from hotel.models import Hotel
from django.urls import reverse
# Create your views here.


def index(request):
    search_term = None
    try:
        search_term = request.POST['search_for_city']
        hotel_list = Hotel.objects.filter(location__iregex=r'^{}'.format(search_term))
    except Exception as e:
        hotel_list = Hotel.objects.all()

    context = {
        'hotel_list': hotel_list,
        'search_term': search_term
    }
    return render(request, "hotel/index.html", context)


def details(request, hotel_id):

        hotel = get_object_or_404(Hotel, pk=hotel_id)

        context = {
            "hotel": hotel
        }
        return render(request, "hotel/details.html", context)


def create(request):
    return render(request, 'hotel/create.html')


def submit(request):
    name = request.POST['name']
    location = request.POST['location']
    hotel = Hotel(name=name, location=location)
    hotel.save()
    return HttpResponseRedirect(reverse('hotel:list'))


def delete(hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    hotel.delete()
    return HttpResponseRedirect(reverse('hotel:list'))


def update(request, hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    new_name = request.POST['name']
    new_location = request.POST['location']
    hotel.name = new_name
    hotel.location = new_location
    hotel.save()
    return HttpResponseRedirect(reverse('hotel:details', args=(hotel_id,)))



