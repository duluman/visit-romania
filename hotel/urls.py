from django.urls import path
from hotel.views import (index,
                         details,
                         create,
                         submit,
                         delete,
                         update,
                         success,
                         room_view,
                         random_hotel,
                         AddRoomPriceView,
                         reservation_view,
                         AddRoom,
                         # create_review,
                         AddHotelReview
                         # submit_review
                         )

app_name = 'hotel'

urlpatterns = [
    path('', view=index, name='list'),
    path('random', view=random_hotel, name='random'),
    path('<int:hotel_id>', view=details, name='details'),
    path('create', view=create, name='create'),
    path('submit', view=submit, name='submit'),
    path('delete/<int:hotel_id>', view=delete, name='delete'),
    path('update/<int:hotel_id>', view=update, name='update'),
    # path('<int:hotel_id>/create_review/', view=create_review, name='create_review'),
    # path('submit_review/', view=submit_review, name='submit_review'),
    path('success', view=success, name='success'),
    path('<int:hotel_id>/room/', view=room_view, name='room'),
    path('room/update/<int:pk>/', AddRoomPriceView.as_view(), name='price_update'),
    path('<int:hotel_id>/room/add/', AddRoom.as_view(), name='create_room'),
    path('review', AddHotelReview.as_view(), name='review'),
    path('reservation', view=reservation_view, name='reservation')]

