from django import forms
from users.models import MyUser, Profile, Homework
from django.urls import path


class MyUserCreationFrom(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name', 'email']

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput,
        label='Type password',
        max_length=255)
    password_confirm = forms.CharField(
        required=True,
        widget=forms.PasswordInput,
        label='Confirm password',
        max_length=255)


class LoginForm(forms.Form):
    email = forms.EmailField(required=True, label='E-mail')
    password = forms.CharField(
        required=True,
        max_length=255,
        label='Password',
        widget=forms.PasswordInput,)


class RegisterForm(forms.Form):
    first_name = forms.CharField(required=True, max_length=255, label='First Name')
    last_name = forms.CharField(required=True, max_length=255, label='Last Name')
    email = forms.EmailField(required=True, label='E-mail')
    password = forms.CharField(
        required=True,
        max_length=255,
        label='Password',
        widget=forms.PasswordInput, )
    password_confirm = forms.CharField(
        required=True,
        widget=forms.PasswordInput,
        label='Confirm password',
        max_length=255)


class UploadFileForm(forms.Form):
    my_file = forms.FileField(required=True)


class UploadProfileImage(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']


class UploadTema(forms.ModelForm):
    class Meta:
        model = Homework
        exclude = []
    # with open(path, 'w+') as page:
    #     for line in page:
    #         show = line.split(", ")
    #         for letter in show:
    #             if letter not in ",":
    #                 print(letter, end=" ")
