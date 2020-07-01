from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.http import HttpResponseRedirect
from hotel.models import Hotel, Room
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import random
# from hotel.forms import  RoomForm #HotelForm

# Create your views here.


def index(request):
    search_term = ''
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


def random_hotel(request):
    hotel_list = Hotel.objects.all()
    print("*****************")
    print(hotel_list)
    print("*****************")

    magician = random.choice(hotel_list)

    context = {

        'rand_location': magician
    }
    return render(request, "hotel/random_location.html", context)


def details(request, hotel_id):

        hotel = get_object_or_404(Hotel, pk=hotel_id)

        context = {
            "hotel": hotel
        }
        return render(request, "hotel/details.html", context)


@login_required
def create(request):

    return render(request, 'hotel/create.html')


@login_required
def submit(request):
    name = request.POST['name']
    owner = request.POST['owner']
    # room = request.POST['room']
    location = request.POST['location']
    review = request.POST['review']
    youtube_video = request.POST['youtube_video']
    hotel = Hotel(name=name, owner=owner, location=location, review=review, youtube_video=youtube_video)
    hotel.save()
    messages.success(request, 'Indeed you added a Hotel')
    return HttpResponseRedirect(reverse('hotel:list'))


@login_required
def delete(request, hotel_id):

    hotel = get_object_or_404(Hotel, pk=hotel_id)
    print(hotel_id)
    hotel.delete()
    messages.success(request, f'You just deleted hotel: {hotel}')
    return HttpResponseRedirect(reverse('hotel:list'))


@login_required
def update(request, hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    print(hotel_id)
    new_name = request.POST['name']
    new_location = request.POST['location']
    new_owner = request.POST['owner']
    new_review = request.POST['review']
    new_youtube_video = request.POST['youtube_video']
    hotel.name = new_name
    hotel.location = new_location
    hotel.owner = new_owner
    hotel.review = new_review
    hotel.youtube_video = new_youtube_video
    hotel.save()
    messages.success(request, 'The update is completed')
    return HttpResponseRedirect(reverse('hotel:details', args=(hotel_id,)))

#todo upload picture form the staff administration page
# def upload_picture_view(request):
#     if request.method == 'POST':
#         form = HotelForm(request.POST, request.FILES)
#
#         if form.is_valid():
#             form.save()
#             return redirect('success')
#     else:
#         form = HotelForm()
#     return render(request, 'upload.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')


# def room_view(request, room_id):
#     room = get_object_or_404(RoomForm, pk=room_id)
#     # form = RoomForm(request.POST, pk=room_id)
#     context = {'room': room}
#     return render(request, "hotel/room.html", context)


def room_view(request, hotel_id):

    room_list = Room.objects.filter(hotel_id=hotel_id)

    context = {
        'room_list': room_list,
        'hotel_id': hotel_id}
    return render(request, "hotel/room.html", context)


# def room_add(request, hotel_id):
#     # hotel_id = hotel_id
#     hotel_id = request.POST['hotel_id']
#     name = request.POST['name']
#     room_type = request.POST['room_type']
#     bathroom = request.POST['bathroom']
#     balcony = request.POST['balcony']
#     # room_picture = request.POST['room_picture']
#     room = Room(hotel_id=hotel_id, name=name, room_type=room_type, bathroom=bathroom, balcony=balcony)
#     room.save()
#
#     return HttpResponseRedirect(reverse('hotel:room', hotel_id))


def messages_test(request):
    messages.success(request, 'Indeed you added a Hotel')

    hotel_all = " This are all the hotels: "

    context = {
        "hotel": hotel_all
    }
    return render(request, "hotel/test_mess.html", context)

