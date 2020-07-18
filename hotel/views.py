from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.http import HttpResponseRedirect
from hotel.models import Hotel, Room, Period
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


# @login_required
def room_view(request, hotel_id):

    room_list = Room.objects.filter(hotel_id=hotel_id)
    # period_list = Period.objects.filter(room_id=room_id)
    # period_list = Period.objects.all()

    period_list = Period.objects.all()

    # for ppperiod in period_list:
    #     for room in room_list:
    #     # print("--------------------")
    #     # print(f"--------------------{room}")
    #     #
    #     # test_room = room.id
    #     # print(f"-------------------- ===== {test_room}")
    #     # period_list = Period.objects.filter(room=room.id)
    #
    #         # print(f"--------------------{room.name}")
    #         print(f"--------------------                {ppperiod.room}")
    #         print(f"--------------------{room.name}")
    #         p_room = str(ppperiod.room)
    #         r_room = str(room.name)
    #
    #         if r_room == p_room:
    #
    #             obj_period = ppperiod
    #             print("OK")
    #             return obj_period



        # print(f"--------------------                {period_list}")
        # print(period_list)
        # print("--------------------")



    # for room in room_list:
    #     # pk = room.id
    #
    #     period_obj = get_object_or_404(Period)
    #     # if period_obj.days > 1:
    #     #     period_obj.total = period_obj.price * period_obj.days
    #     # print("--------------------")
    #     # print(period_obj)
    #     # print("--------------------")


    context = {
        'room_list': room_list,
        'hotel_id': hotel_id,
        # 'room_id': room_id,
        'period_list': period_list,
        # 'period_list': period_obj,
    }
    return render(request, "hotel/room.html", context)


# def update_room_price(request, hotel_id):
#     room_list = Room.objects.filter(hotel_id=hotel_id)
#     period_list = Period.objects.all()
#     print(period_list)
#     for room in room_list:
#         for ppperiod in period_list:
#             # print("OK | " * 14)
#             print("OK | " * 7)
#             print(room.id)
#             print("OK | " * 7)
#             print(ppperiod.room_id)
#             new_total = request.POST['total']
#     return HttpResponseRedirect(reverse('hotel:room', args=(hotel_id,)))


@login_required
def create_room_view(request, hotel_id):

    return render(request, 'hotel/room_add_ok.html')


# @login_required
# def room_add(request, hotel_id):
#
#     name = request.POST['name']
#     room_type = request.POST['room_type']
#     bathroom = request.POST['bathroom']
#     balcony = request.POST['balcony']
#
#     room = Room(hotel_id=hotel_id, name=name, room_type=room_type, bathroom=bathroom, balcony=balcony, room_picture=None)
#     room.save()
#     return HttpResponseRedirect(reverse('hotel:room', args=(hotel_id, )))


# def messages_test(request):
#     messages.success(request, 'Indeed you added a Hotel')
#
#     hotel_all = " This are all the hotels: "
#
#     context = {
#         "hotel": hotel_all
#     }
#     return render(request, "hotel/test_mess.html", context)

