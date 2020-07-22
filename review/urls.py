from django.urls import path
from review.views import app_review_view, AddReviewView


app_name = 'review'

urlpatterns = [
    path('', view=app_review_view, name='app_review'),
    path('add', AddReviewView.as_view(), name='add_review')
]

