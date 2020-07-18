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
                         # room_add,
                         create_room_view,
                         # update_room_price
                         ) # room_add #,upload_picture_view messages_test
#
app_name = 'hotel'

urlpatterns = [
    path('', view=index, name='list'),
    path('random', view=random_hotel, name='random'),
    path('<int:hotel_id>', view=details, name='details'),
    path('create', view=create, name='create'),
    path('submit', view=submit, name='submit'),
    path('delete/<int:hotel_id>', view=delete, name='delete'),
    path('update/<int:hotel_id>', view=update, name='update'),
    # path('upload', view=upload_picture_view, name='upload'),
    path('success', view=success, name='success'),
    path('<int:hotel_id>/room', view=room_view, name='room'),
    # path('<int:hotel_id>/room/update', view=update_room_price, name='update_price'),
    # path('<int:hotel_id>/room/room_add/', view=room_add, name='room_add'),
    path('<int:hotel_id>/room/add/', view=create_room_view, name='create_room_view'),
    # path('t', view=messages_test, name='t'),
]
