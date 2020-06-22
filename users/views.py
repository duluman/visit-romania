
from django.core.mail import EmailMultiAlternatives
from users.admin import MyUserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from django.conf import settings
from users.forms import LoginForm, UploadFileForm, UploadProfileImage #ContactForm, ChangePasswordForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from helpers.upload import handle_upload_file
from django.template.loader import get_template
# from django.contrib.sites.models import Site #v1 din register


def handle_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = LoginForm()

    return render(request, 'users/login.html', {
        'form': form
    })


def handle_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))


@login_required
def profile(request):
    if request.method == 'POST':
        user_profile = request.user.profile
        form = UploadProfileImage(request.POST, request.FILES, instance=user_profile)

        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            return HttpResponseRedirect(reverse('users:profile'))

    else:
        form = UploadProfileImage()

    return render(request, 'users/profile.html', {'form': form})


@login_required
def profile_email(request):

    email_template = get_template('users/email.html')
    email_content = email_template.render(
        {
            'your_profile': request.user.profile,
            'your_email': request.user.email,
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
        })

    mail = EmailMultiAlternatives(
        'Your profile data request',
        email_content,
        settings.EMAIL_HOST_USER,
        [request.user.email])

    mail.content_subtype = 'html'
    mail.attach_file('{BASE_DIR}/{MEDIA_ROOT}/{PROFILE_IMAGE}'.format(
        BASE_DIR=settings.BASE_DIR,
        MEDIA_ROOT=settings.MEDIA_ROOT,
        PROFILE_IMAGE=request.user.profile.avatar))
    mail.send()

    return HttpResponseRedirect(reverse('users:profile'))


def register(request):
    # current_site = Site.objects.get_current()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = MyUserCreationForm()

    return render(request, 'users/register.html', {
                        # 'host': current_site.domain,
                        'form': form
                   })


#inca nu am folosit acest view
def upload(request):

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            my_file = form.cleaned_data['my_file']
            handle_upload_file(my_file)
    else:
        form = UploadFileForm()
    return render(request, 'users/upload.html', {'form': form})


def contact_view(request):
    # form = ContactForm(request.POST)
    # if form.is_valid():
    #     return render(request, 'users/contact.html', {'form': form})

    return render(request, "users/contact.html")


# @login_required
# def change_password(request):
#     form = ChangePasswordForm(request.POST)
#     if request.method == 'POST':
#         if form.is_valid():
#             new_password = form.cleaned_data['new_password']
#             confirm_password = form.cleaned_data['confirm_password']
#             # password = form.cleaned_data['password']
#             if new_password == confirm_password:
#                 # password = confirm_password
#                 return HttpResponseRedirect(reverse('users:profile'))
#
#     return render(request, "users/change_password.html", {'form': form})

#
# <form method="post" action="{% url 'users:change_password'  %}">
#                 {% csrf_token %}
#                 {{ form.as_p }}
#     <input type="submit" class="btn btn-primary mb-2" value="Change password" />
# </form>