

from users.forms import MyUserCreationFrom
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse

from users.forms import LoginForm, UploadFileForm, UploadProfileImage, UploadTema
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from helpers.upload import handle_upload_file


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


def register(request):
    if request.method == 'POST':
        form = MyUserCreationFrom(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = MyUserCreationFrom()

    return render(request, 'users/register.html', {
                       'form': form
                   })


def upload(request):

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            my_file = form.cleaned_data['my_file']
            handle_upload_file(my_file)
    else:
        form = UploadFileForm()
    return render(request, 'users/upload.html', {'form': form})


def upload_tema(request):
    if request.method == 'POST':
        form = UploadTema(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = UploadTema()

    return render(request, 'users/tema.html', {'form': form})
