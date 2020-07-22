from django.shortcuts import render
from review.models import AppReview
from django.views.generic import CreateView

# Create your views here.


def app_review_view(request):
    review_objects = AppReview.objects.all()

    context = {
        'review_list': review_objects
    }

    return render(request, 'review/app_review.html', context)


class AddReviewView(CreateView):
    model = AppReview
    template_name = 'review/add_review.html'
    fields = ['name', 'comment', 'stars']
