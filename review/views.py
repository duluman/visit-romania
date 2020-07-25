from django.shortcuts import render
from review.models import AppReview
from django.views.generic import CreateView
from django import forms
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.


def app_review_view(request):
    review_objects = AppReview.objects.all()
    review_count = AppReview.objects.all().count()

    context = {
        'review_list': review_objects,
        'count_app': review_count
    }

    return render(request, 'review/app_review.html', context)


@method_decorator(login_required, name='dispatch')
class AddReviewView(CreateView):
    model = AppReview
    template_name = 'review/add_review.html'
    fields = ['comment', 'stars']

    def get_initial(self):
        initial = {'name': self.request.user}
        return initial

    # Add name to form data before setting it as valid (so it is saved to model)
    def form_valid(self, form):
        # Add logged-in user as name
        form.instance.name = self.request.user
        # Call super-class form validation behaviour
        return super(AddReviewView, self).form_valid(form)





    # def get_initial(self):
    #     # initial = super(AddReviewView, self).get_initial()
    #       initial['name'] = self.request.user
    #
    #     return initial

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get the context
    #     context = super(AddReviewView, self).get_context_data(**kwargs)
    #     # Create any data and add it to the context
    #     context['name_id'] = self.request.user
    #     return context


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
