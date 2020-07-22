from django.urls import path
from users.views import (register, profile,
                         handle_login,
                         handle_logout,
                         profile_email,
                         contact_view,
                         change_password
                         )


app_name = 'users'

urlpatterns = [

    path('register/', view=register, name='register'),
    path('login/', view=handle_login, name='login'),
    path('logout/', view=handle_logout, name='logout'),
    path('contact/', view=contact_view, name='contact'),
    path('profile/', view=profile, name='profile'),
    path('profile/email', view=profile_email, name='profile_email'),
    path('change_password/', view=change_password, name='change_password'),
    ]


