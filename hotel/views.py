from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import HttpResponseRedirect
from hotel.models import Hotel, Room, Period, CustomerReview, BadgeHotel, BestFeature
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import random
from django.views.generic import UpdateView, CreateView
from django.utils.decorators import method_decorator
# from hotel.forms import AddHotelReviewForm

# Create your views here.


def index(request):
    search_term = ''
    badge_list = BadgeHotel.objects.all()
    number_of_hotels = Hotel.objects.all().count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    try:
        search_term = request.POST['search_for_city']
        hotel_list = Hotel.objects.filter(location__iregex=r'^{}'.format(search_term))
    except Exception as e:
        hotel_list = Hotel.objects.all()

    context = {
        'hotel_list': hotel_list,
        'search_term': search_term,
        'badge_list': badge_list,
        'hotel_count': number_of_hotels,
        'num_visits': num_visits}

    return render(request, "hotel/index.html", context)


def random_hotel(request):
    hotel_list = Hotel.objects.all()
    magician = random.choice(hotel_list)
    badge_list = BadgeHotel.objects.all()
    context = {'rand_location': magician,
               'badge_list': badge_list}

    return render(request, "hotel/random_location.html", context)


def details(request, hotel_id):

        hotel = get_object_or_404(Hotel, pk=hotel_id)
        review_list = CustomerReview.objects.filter(hotel_to_review_id=hotel_id)
        best_feature_list = BestFeature.objects.filter(hotel_feature_id=hotel_id)

        context = {
            "hotel": hotel,
            "review_list": review_list,
            "best_feature_list": best_feature_list}

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


# def create_review(request, hotel_id):
#     return render(request, 'hotel/create_review.html')


# def submit_review(request, hotel_id):
#
#     # customer = request.user
#     hotel_to_review = Hotel.objects.filter(hotel_id=hotel_id)
#     # hotel_to_review = get_object_or_404(Hotel, pk=hotel_id)
#     # hotel_to_review = request.POST['hotel_to_review']
#     # hotel_to_review = request.get['hotel_id':hotel_id]
#     comment = request.POST['comment']
#     stars = request.POST['stars']
#     { % url    'hotel:submit_review'    hotel_id %}
#     print("*** hotel name ***")
#     # print(hotel_to_review)
#     print("*** hotel name ***")
#
#     # {% url 'hotel:submit_review' hotel_id %}
#     customerreview = CustomerReview(hotel_to_review= hotel_to_review, comment=comment, stars=stars)
#     customerreview.save()
#     messages.success(request, 'Indeed you added a Review')
#     return HttpResponseRedirect(reverse('hotel:list'))

# def submit_review(request, hotel_id):
#     pass
#     # customer = request.user
#     hotel_to_review = "How to get the hotel review"
#     comment = request.POST['comment']
#     stars = request.POST['stars']
#     print(hotel_id)
#     print("*** hotel name ***")
#     # print(comment)
#     # print(stars)
#     # print(customer)
#     print(hotel_to_review)
#     # for hotel in hotel_to_review:
#     #     print(hotel.name)
#     # return HttpResponseRedirect(reverse('hotel:details', args=(hotel_id,)))
#     # {% url 'hotel:submit_review' hotel_id %}
#     customerreview = CustomerReview(comment=comment, stars=stars)
#     customerreview.save()
#     messages.success(request, 'Indeed you added a Review')
#     return HttpResponseRedirect(reverse('hotel:details', args=(hotel_id,)))


def room_view(request, hotel_id):

    room_list = Room.objects.filter(hotel_id=hotel_id)
    period_list = Period.objects.all()

    context = {
        'room_list': room_list,
        'hotel_id': hotel_id,
        'period_list': period_list}

    return render(request, "hotel/room.html", context)


@method_decorator(login_required, name='dispatch')
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


@method_decorator(login_required, name='dispatch')
class AddRoom(CreateView):
    model = Room
    fields = '__all__'
    template_name = 'hotel/room_add.html'

    # def get_initial(self):
    #     initial = super(AddRoom, self).get_initial()
    #     print("$-$-$-$-$-$-$-$-$-$-$-$-$-$-$-$-$-$-$-$-$-$")
    #     print(self.request.user)
    #     print(initial)
    #     print("$-$-$-$-$-$-$-$-$-$-$-$-$-$-$-$-$-$-$-$-$-$")
    #     initial['customer'] = self.request.user


@method_decorator(login_required, name='dispatch')
class AddHotelReview(CreateView):
    model = CustomerReview
    # fields = "__all__"
    fields = ["hotel_to_review", "comment", "stars"]
    template_name = "hotel/add_review.html"

    def get_initial(self):
        initial = super(AddHotelReview, self).get_initial()
        print(self.request.user)
        initial['customer'] = self.request.user

        return initial

    def form_valid(self, form):
        form.instance.customer = self.request.user

        return super(AddHotelReview, self).form_valid(form)



