from django.urls import path
from payments.views import view_cards, add_card, delete_card

app_name = 'payments'

urlpatterns = [
    path('cards/', view=view_cards, name='view_cards'),
    path('cards/add', view=add_card, name='add_card'),
    path('cards/delete/<str:card_id>/', view=delete_card, name='delete_card')
]