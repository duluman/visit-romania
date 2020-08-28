from django.urls import path
from adoptions.views import pet_view, pet_details, pet_test_variable_view

app_name = 'adoptions'

urlpatterns = [
    path('pets/', view=pet_view, name='pets'),
    path('test/', view=pet_test_variable_view, name='test'),
    path('adoptions/<int:pet_id>/', view=pet_details, name='pet')
]