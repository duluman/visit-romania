from django.shortcuts import render, Http404, HttpResponseRedirect, reverse, get_object_or_404
from django.conf import settings
import stripe
from django.contrib.auth.decorators import login_required
from payments.models import StripeCard
# Create your views here.


@login_required
def view_cards(request):

    cards_detail = stripe.Customer.list_sources(
        request.user.stripe_data.customer_id,
        api_key=settings.STRIPE_SECRET_KEY
    )

    return render(request, 'payments/view_cards.html', {
        'cards': cards_detail['data']
    })


    # if cards_detail['has_more'] == True: #it can be added to handle customers with more than 10 cards
    #     more_cards_detail = stripe.Customer.list_sources(
    #         request.user.stripe_data.customer_id,
    #         starting_after=cards_detail['data'][-1]['id'],
    #         # from the list of cards we will take the last one ID
    #         api_key=settings.STRIPE_SECRET_KEY
    # )


@login_required
def add_card(request):

    if request.method == 'GET':
        return render(request, 'payments/add_card.html', {'stripe_key': settings.STRIPE_PUBLIC_KEY})
        # we make request from the web page

    else:
        if 'stripeToken' in request.POST:
            stripe_token = request.POST['stripeToken']
            card = stripe.Customer.create_source(
                request.user.stripe_data.customer_id,
                source=stripe_token,
                api_key=settings.STRIPE_SECRET_KEY# because we make request from the app
            )

            StripeCard(customer=request.user.stripe_data, card_id=card['id']).save()

            return HttpResponseRedirect(reverse('payments:view_cards'))

        raise Http404


# @login_required
# def add_card_refactor(request):
#     stripe_customer = request.user.stripe_data
#     if request.method == 'GET':
#         return render(request, 'payments/add_card.html', {'stripe_key': settings.STRIPE_PUBLIC_KEY})
#         # we make request from the web page
#
#     else:
#         if 'stripeToken' in request.POST:
#             stripe_token = request.POST['stripeToken']
#             card = stripe.Customer.create_source(
#                 stripe_customer.customer_id,
#                 source=stripe_token,
#                 api_key=settings.STRIPE_SECRET_KEY  # because we make request from the app
#             )
#
#             StripeCard(customer=stripe_customer, card_id=card['id']).save()
#
#             return HttpResponseRedirect(reverse('payments:view_cards'))
#
#         raise Http404


@login_required()
def delete_card(request, card_id):
    # if request.method == 'POST':
    if request.POST:
        stripe_customer = request.user.stripe_data

        card = get_object_or_404(StripeCard, customer=stripe_customer, card_id=card_id)

        stripe.Customer.delete_source(
            stripe_customer.customer_id,
            card_id,
            api_key=settings.STRIPE_SECRET_KEY
        )

        card.delete()

        return HttpResponseRedirect(reverse('payments:view_cards'))

    raise Http404

