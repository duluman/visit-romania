from django.urls import path
from hotel.views import index, details, create, submit, delete, update

app_name = 'hotel'

urlpatterns = [
    path('', view=index, name='list'),
    path('<int:hotel_id>', view=details, name='details'),
    path('create', view=create, name='create'),
    path('submit', view=submit, name='submit'),
    path('delete/<int:hotel_id>', view=delete, name='delete'),
    path('update/<int:hotel_id>', view=update, name='update'),
]
