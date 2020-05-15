from django.urls import path
from users.views import register, profile, handle_login, handle_logout, upload, upload_tema

app_name = 'users'

urlpatterns = [
    # path('', view=homepage, name='homepage')
    path('register/', view=register, name='register'),
    path('login/', view=handle_login, name='login'),
    path('logout/', view=handle_logout, name='logout'),
    path('profile/', view=profile, name='profile'),
    path('upload/', view=upload, name='upload'),
    path('tema/', view=upload_tema, name='tema')]
