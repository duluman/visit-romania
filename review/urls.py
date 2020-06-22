from django.urls import path
from review.views import index


app_name = 'review'

urlpatterns = [
    path('', view=index)]
