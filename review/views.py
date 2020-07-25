from django.shortcuts import render
from review.models import AppReview
from django.views.generic import CreateView
from django import forms
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

    # def get(self, request, *args, **kwargs):
    #     form = super(AddReviewView, self).get_form()
    #
    #     initial_base = self.get_initial()
    #     initial_base['name'] = request.user.email
    #     form.initial = initial_base
    #     form.fields['name'].widget = forms.widgets.EmailInput()
    #     # return response using standard render() method
    #     return render(request, self.template_name,
    #                   {'form': form})
