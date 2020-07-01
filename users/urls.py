from django.urls import path
from users.views import (register, profile,
                         handle_login,
                         handle_logout,
                         upload,
                         profile_email,
                         contact_view, change_password, reset_password
                         )

from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    # path('', view=homepage, name='homepage')
    path('register/', view=register, name='register'),
    path('login/', view=handle_login, name='login'),
    path('logout/', view=handle_logout, name='logout'),
    path('contact/', view=contact_view, name='contact'),
    path('profile/', view=profile, name='profile'),
    path('profile/email', view=profile_email, name='profile_email'),
    path('change_password/', view=change_password, name='change_password'),
    path('reset_password/', view=reset_password, name='reset_password'),
    path('upload/', view=upload, name='upload')]
    # path('password_change/done/',
    #      auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
    #      name='password_change_done'),
    #
    # path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'),
    #      name='password_change'),
    #
    # path('password_reset/done/',
    #      auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
    #      name='password_reset_done'),
    #
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    #
    # path('reset/done/',
    #      auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
    #      name='password_reset_complete')]

