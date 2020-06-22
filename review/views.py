from django.shortcuts import render
from review.models import Review

# Create your views here.


def index(request):
    review_list = Review.objects.all()

    context = {
        'review_list': review_list
    }

    return render(request, 'review/index.html', context)
