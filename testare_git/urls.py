"""testare_git URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from testare_git.views import home_page, read_more
from django.conf import settings
from django.conf.urls.static import static

# you can change the header am title form de admin page
admin.site.site_header = " Visit Romania Admin"
admin.site.site_title = " Admin "


urlpatterns = [
    path('admin/', admin.site.urls, name='admin_view'),
    path('', view=home_page),
    path('read_more/', view=read_more),
    path('hotel/', include("hotel.urls")),
    path('review/', include("review.urls")),
    path('users/', include("users.urls")),
    path('users/activate/', include("activation.urls")),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('payments/', include("payments.urls")),
    path('adoptions/', include("adoptions.urls")),
    path('about_me/', include("jobs.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
