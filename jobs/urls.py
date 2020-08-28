from django.urls import path
from jobs.views import nick_view

app_name = 'jobs'

urlpatterns = [
    path('', view=nick_view, name='cristian')]
