from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import HttpResponseRedirect
from hotel.models import Hotel, Room, Period, CustomerReview
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import random
from django.views.generic import UpdateView, CreateView


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
        'search_term': search_term}

    return render(request, "hotel/index.html", context)


def random_hotel(request):
    hotel_list = Hotel.objects.all()
    magician = random.choice(hotel_list)
    context = {'rand_location': magician}

    return render(request, "hotel/random_location.html", context)


def details(request, hotel_id):

        hotel = get_object_or_404(Hotel, pk=hotel_id)
        review_list = CustomerReview.objects.filter(hotel_to_review_id=hotel_id)

        context = {
            "hotel": hotel,
            "review_list": review_list
        }
        return render(request, "hotel/details.html", context)


@login_required
def create(request):

    return render(request, 'hotel/create.html')


@login_required
def submit(request):
    name = request.POST['name']
    owner = request.POST['owner']
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


def success(request):
    return HttpResponse('successfully uploaded')


def create_review(request, hotel_id):
    return render(request, 'hotel/create_review.html')


def submit_review(request, hotel_id):
    customer = request.user
    hotel_to_review = "How to get the hotel review"
    # comment = request.POST['comment']
    # stars = request.POST['stars']
    print(hotel_id)
    print("*** hotel name ***")
    # print(comment)
    # print(stars)
    print(customer)
    print(hotel_to_review)
    # for hotel in hotel_to_review:
    #     print(hotel.name)
    return HttpResponse('Submit view review')
    #
    # customerreview = CustomerReview(comment=comment, stars=stars)
    # customerreview.save()
    # messages.success(request, 'Indeed you added a Review')
    # return HttpResponseRedirect(reverse('hotel:details', args=(hotel_id,)))


def room_view(request, hotel_id):

    room_list = Room.objects.filter(hotel_id=hotel_id)
    period_list = Period.objects.all()

    context = {
        'room_list': room_list,
        'hotel_id': hotel_id,
        'period_list': period_list}

    return render(request, "hotel/room.html", context)


class AddRoomPriceView(UpdateView):
    model = Period
    fields = ['days']
    # fields = ['days', 'seasons']
    template_name = 'hotel/update_price.html'


@login_required
def reservation_view(request):

    print("$$$$$$$$$$$$$$$$$$$$$$")

    template = 'hotel/reservation.html'
    if request.POST:
        context = {'reservation_context': ' Done!'}
    else:
        context = {'reservation_context': ' Whar are you doing here?!'}

    return render(request, template, context)


class AddRoom(CreateView):
    model = Room
    fields = '__all__'
    template_name = 'hotel/room_add.html'


