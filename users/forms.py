from django import forms
from users.models import MyUser, Profile
from django.contrib.auth import password_validation
# from activation.signals import set_inactive_user
# from django.conf import settings


# class MyUserCreationForm(forms.ModelForm):
#     class Meta:
#         model = MyUser
#         fields = ['first_name', 'last_name', 'email']
#
#     password1 = None
#     password2 = None
#
#     def clean_password2(self):
#         pass
#
#     def _post_clean(self):
#         pass
#
#     # def save(self, commit=True):
#     #     first_name = self.cleaned_data['first_name']
#     #     last_name = self.cleaned_data['last_name']
#     #     email = self.cleaned_data['email']
#     #     user = MyUser.objects.create_user(email, first_name, last_name)
#     #     return user
#
#     def save(self, commit=True):
#         user = super(forms.ModelForm, self).save(commit=False)
#         email = self.cleaned_data.get('email')
#         first_name = self.cleaned_data.get('first_name')
#         last_name = self.cleaned_data.get('last_name')
#
#         user.email = email
#         user.first_name = first_name
#         user.last_name = last_name
#         set_inactive_user.send(sender=settings.AUTH_USER_MODEL, user=user)
#         if commit:
#
#             user.save()
#         # user = MyUser.objects.create_user(email, first_name, last_name)
#
#         return user


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
        widget=forms.PasswordInput,
    )
    password_confirm = forms.CharField(
        required=True,
        max_length=255,
        label='Confirm password',
        widget=forms.PasswordInput,
    )

    def clean_email(self):
        email = self.cleaned_data['email']
        users = MyUser.objects.filter(email=email)

        if users.count() != 0:
            raise forms.ValidationError('E-mail already exists.')

        return email

    def clean_password_confirm(self):
        password = self.cleaned_data['password']
        password_confirm = self.cleaned_data['password_confirm']

        if password_confirm != password:
            raise forms.ValidationError("Password confirm doesn't match")

        return password_confirm

    def save(self):
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        user = MyUser.objects.create_user(email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()


class UploadFileForm(forms.Form):
    my_file = forms.FileField(required=True)


class UploadProfileImage(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']


class SetPassword(forms.Form):
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput,
        help_text=password_validation.password_validators_help_text_html())
    password_confirmation = forms.CharField(required=True, widget=forms.PasswordInput)

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def clean_password(self):
        password = self.cleaned_data.get('password')
        password_validation.validate_password(password, self.user)
        return password

    def clean_password_confirmation(self):
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')

        if password_confirmation != password:
            raise forms.ValidationError('Password mismatch')

        return password_confirmation

    def save(self, commit=True):
        password = self.cleaned_data.get('password')
        self.user.set_password(password)

        if commit:
            self.user.save()

        return self.user


class ContactForm(forms.Form):
    first_name = forms.CharField(required=True, max_length=255, label='First Name')
    last_name = forms.CharField(required=True, max_length=255, label='Last Name')
    email = forms.EmailField(required=True, label='E-mail')
    mobile = forms.CharField(required=False, max_length=20, label='Mobile Phone')
    subject = forms.CharField(required=True, max_length=255, label='Subject')
    message = forms.CharField(required=True, min_length=30, max_length=1000, label='Your message')



# class ChangePasswordForm(forms.Form):
#     password = forms.CharField(
#         required=True,
#         max_length=255,
#         label='Current Password',
#         widget=forms.PasswordInput)
#
#     new_password = forms.CharField(
#         required=True,
#         max_length=23,
#         label='New Password',
#         widget=forms.PasswordInput)
#     confirm_password = forms.CharField(
#         required=True,
#         max_length=23,
#         label='Confirm password',
#         widget=forms.PasswordInput)
#
#     def __init__(self, user, *args, **kwargs):
#         self.user = user
#         super().__init__()
#
#     def clean_password_confirm(self):
#
#         new_password = self.cleaned_data['new_password']
#         confirm_password = self.cleaned_data['confirm_password']
#
#         if confirm_password != new_password:
#             raise forms.ValidationError("Password confirm doesn't match")
#
#         password_validation.validate_password(confirm_password, self.user)
#         password = confirm_password
#         return password
#
#     def save(self, commit=True):
#
#         password = self.cleaned_data['password']
#         self.user.set_password(password)
#         print("****" * 8)
#         print(password)
#         print("****" * 8)
#         if commit:
#             self.user.save(password=password)
#         return self.user
