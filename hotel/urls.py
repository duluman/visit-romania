from django.urls import path
from hotel.views import index, details, create, submit, delete, update, success, room_view# room_add #,upload_picture_view
#
app_name = 'hotel'

urlpatterns = [
    path('', view=index, name='list'),
    path('<int:hotel_id>', view=details, name='details'),
    path('create', view=create, name='create'),
    path('submit', view=submit, name='submit'),
    path('delete/<int:hotel_id>', view=delete, name='delete'),
    path('update/<int:hotel_id>', view=update, name='update'),
    # path('upload', view=upload_picture_view, name='upload'),
    path('success', view=success, name='success'),
    path('<int:hotel_id>/room', view=room_view, name='room'),
    # path('room_add', view=room_add, name='room_add'),
]
